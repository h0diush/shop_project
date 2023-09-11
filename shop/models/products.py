from django.db import models

from shop.models import Category


class Product(models.Model):
    """Таблица "Продукт"
    category - Категория: Кофе
    name - Название: Nestle
    slug - Ссылка: nestle
    price - Цена: 19.99
    available - В наличии: True
    description - Описание: вкусный насыщенный аромат
    created -
    updated -
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="products",
                                 verbose_name="Категория", )
    name = models.CharField("Название", max_length=155)
    slug = models.SlugField(verbose_name="Ссылка", unique=True, max_length=155)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField("Описание")
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Изменено", auto_now=True)
    available = models.BooleanField("В наличии", default=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["-created"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name
