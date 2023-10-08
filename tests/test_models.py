from decimal import Decimal

from common.tests.mixins import TestMixin
from orders.models import Order, OrderItem


class TestModel(TestMixin):

    def _order_create(self):
        order = Order.objects.create(**self.order_data)
        order.save()
        return order

    def test_model_product(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_model_category(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_model_order(self):
        order = self._order_create()
        expected_str = f"Заказ № {order.pk}"
        self.assertEqual(str(order), expected_str)

    def test_model_order_item(self):
        order_item_data = {
            'order': self._order_create(),
            'product': self.product,
            'price': Decimal(9.99),
            'quantity': 3
        }
        order_item = OrderItem.objects.create(**order_item_data)
        order_item.save()
        self.assertEqual(str(order_item), str(order_item.pk))
        result = order_item_data['price'] * order_item_data['quantity']
        self.assertEqual(order_item.get_cost(), result)

    def test_model_coupon(self):
        self.assertEqual(str(self.coupon), self.coupon_data['code'])
