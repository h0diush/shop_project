from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Coupon(models.Model):

    code = models.CharField("Купон", max_length=55, unique=True)
    valid_from = models.DateTimeField("C")
    valid_to = models.DateTimeField("По")
    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        help_text="Введите значение от 0 до 100 %"
    )
    active = models.BooleanField("Активно?")

    class Meta:
        verbose_name = "Купон"
        verbose_name_plural = "Купоны"

    def __str__(self):
        return self.code


