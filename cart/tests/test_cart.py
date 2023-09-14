from decimal import Decimal

from cart.serializers.products import ProductsInCartSerializer
from common.tests.mixins import TestMixin


class TestCartInProduct(TestMixin):

    def test_product_in_cart(self):
        data = {'quantity': '3'}
        end_price_product = round(
            Decimal(self.product.price * int(data['quantity'])), 2)
        response = self.client.post(
            f'/api/shop/products/{self.product.slug}/add_product_in_cart/',
            data)
        self.assertEqual(response.status_code, 200)
        cart = self.client.get('/api/cart/')
        self.assertEqual(cart.status_code, 200)
        self.assertEqual(len(cart.data['items']), 1)
        self.assertEqual(cart.data['end_price'], end_price_product)
        expected_data = ProductsInCartSerializer(self.product)
        self.assertEqual(cart.data['items'][0]['product'], expected_data.data)
        response = self.client.get(
            f'/api/shop/products/{self.product.slug}/remove_product_from_cart/')
        self.assertEqual(response.status_code, 200)
        cart = self.client.get('/api/cart/')
        self.assertEqual(cart.status_code, 200)
        self.assertEqual(len(cart.data['items']), 0)
        self.assertEqual(cart.data['end_price'], 0)
