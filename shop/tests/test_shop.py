from django.test import TestCase
from rest_framework.test import APIClient

from shop.models import Category, Product
from shop.serializers.categories import CategoriesListSerializers, \
    CategoryRetrieveSerializers


class ShopTest(TestCase):

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

    def test_categories_list(self):
        response = self.client.get('/api/shop/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        expected_data = CategoriesListSerializers(Category.objects.all(),
                                                  many=True).data
        self.assertEqual(response.data, expected_data)

    def test_category_retrieve(self):
        response = self.client.get(
            f'/api/shop/categories/{self.category_data["slug"]}/')
        self.assertEqual(response.status_code, 200)
        expected_data = CategoryRetrieveSerializers(
            Category.objects.get(name=self.category_data['name'])).data
        self.assertEqual(response.data, expected_data)
