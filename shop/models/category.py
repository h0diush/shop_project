from django.db import models


class Category(models.Model):
    """Таблица "Категория"
    name - название категории
    slug - ссылка на категорию
    """

    name = models.CharField("Название", max_length=55)
    slug = models.SlugField("Ссылка", max_length=55, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
