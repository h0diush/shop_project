from django.test import TestCase
from rest_framework.test import APIClient

from shop.models import Product, Category


class TestMixin(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.category_data = {
            'name': 'name_category',
            'slug': 'slug_category'
        }
        self.category = Category.objects.create(
            **self.category_data
        )
        self.product_data = {
            'name': 'name_product',
            'slug': 'slug_product',
            'category': self.category,
            'price': 9.99,
            'description': 'test_description'
        }
        self.product = Product.objects.create(
            **self.product_data
        )
