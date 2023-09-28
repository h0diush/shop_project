from django.conf import settings
from django.db import models

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField("Имя", max_length=55)
    last_name = models.CharField("Фамилия", max_length=55)
    email = models.EmailField("Электронная почта")
    address = models.CharField("Адрес", max_length=255)
    postal_code = models.CharField("Индекс", max_length=20)
    city = models.CharField("Город", max_length=75)
    paid = models.BooleanField("Оплачено", default=False)
    stripe_id = models.CharField("Stripe идентификатор", max_length=250,
                                 blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Изменено", auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def __str__(self):
        return f"Заказ № {self.pk}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:
            path = '/test/'
        else:
            path = '/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="items", verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="order_items",
                                verbose_name="Продукт")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f"{self.pk}"

    def get_cost(self):
        return self.price * self.quantity
