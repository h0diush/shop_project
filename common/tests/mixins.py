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
        self.order_data = {
            "first_name": "Aid",
            "last_name": "Jack",
            "email": "wasca@aww.vc",
            "address": "Belgian: Tweak Color RED ",
            "postal_code": "123456",
            "city": "Brussels"
        }

        self.cart_data = {
            'quantity': '3',
            'override': False
        }
