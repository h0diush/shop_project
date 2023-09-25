from common.tests.mixins import TestMixin
from shop.models import Product, Category
from shop.serializers.categories import CategoriesListSerializers, \
    CategoryRetrieveSerializers
from shop.serializers.products import ProductsListSerializers, \
    ProductRetrieveSerializer, ProductAddInCartSerializers


class TestShopSerializer(TestMixin):
    """Тестирование сериализаторов"""

    def test_get_list_products(self):
        response = self.client.get('/api/shop/products/')
        self.assertEqual(response.status_code, 200)
        products_list = Product.objects.all()
        self.assertEqual(response.data,
                         ProductsListSerializers(products_list,
                                                 many=True).data)

    def test_get_retrieve_products(self):
        response = self.client.get(
            f'/api/shop/products/{self.product.slug}/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,
                         ProductRetrieveSerializer(self.product).data)

    def test_get_list_categories(self):
        response = self.client.get(
            '/api/shop/categories/'
        )
        self.assertEqual(response.status_code, 200)
        categories_list = Category.objects.all()
        self.assertEqual(response.data,
                         CategoriesListSerializers(categories_list,
                                                   many=True).data)

    def test_get_list_products_in_category(self):
        response = self.client.get(
            f'/api/shop/categories/{self.category.slug}/'
        )
        self.assertEqual(response.status_code, 200)
        products_list_in_category = self.category.products.all()
        self.assertEqual(response.data,
                         CategoryRetrieveSerializers(self.category).data)
        self.assertEqual(response.data['products'],
                         ProductsListSerializers(products_list_in_category,
                                                 many=True).data)

    def test_product_in_cart(self):
        data = {'quantity': '3', 'override': False}
        serializer = ProductAddInCartSerializers(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data, data)

    def test_validate_quantity_add_product_in_cart(self):
        error_values = [0, -1, 33, 45, 'test']
        for _ in error_values:
            data = {'quantity': _}
            serializer = ProductAddInCartSerializers(data=data)
            self.assertFalse(serializer.is_valid())
            self.assertEqual(set(serializer.errors), {'quantity'})
