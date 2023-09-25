from decimal import Decimal

from cart.serializers.products import ProductsInCartSerializer
from common.tests.mixins import TestMixin
from orders.models import Order
from shop.serializers.products import ProductAddInCartSerializers


class TestCart(TestMixin):

    def _add_product(self, data):
        response = self.client.post(
            f'/api/shop/products/{self.product.slug}/add_product_in_cart/',
            ProductAddInCartSerializers(data).data
        )
        return response

    def test_add_and_remove_product_in_cart(self):
        response = self._add_product(self.cart_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,
                         {
                             'message': f'{self.product.name} добавлен в корзину'})
        cart = self.client.get('/api/cart/')

        self.assertEqual(cart.status_code, 200)
        end_price_product = round(
            Decimal(self.product.price * int(self.cart_data['quantity'])), 2)
        self.assertEqual(len(cart.data['items']), 1)
        self.assertEqual(cart.data['items'][0]['total_price'],
                         end_price_product)
        expected_data = ProductsInCartSerializer(self.product)
        self.assertEqual(cart.data['items'][0]['product'], expected_data.data)
        response = self.client.get(
            f'/api/shop/products/{self.product.slug}/remove_product_from_cart/',
        )
        cart = self.client.get('/api/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cart.data['items']), 0)

    def test_cart_clear(self):
        response = self._add_product(self.cart_data)
        self.assertEqual(response.status_code, 200)
        cart = self.client.get('/api/cart/')
        self.assertEqual(len(cart.data['items']), 1)
        response = self.client.get('/api/cart_clear/')
        cart = self.client.get('/api/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cart.data['items']), 0)

    def test_create_order(self):
        response = self._add_product(self.cart_data)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/orders/', self.order_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], self.order_data['email'])
        orders = Order.objects.all()
        self.assertEqual(len(orders), 1)
        self.assertEqual(len(orders[0].items.all()), 1)
