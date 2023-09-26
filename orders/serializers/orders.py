from rest_framework import serializers

from common.serializers.mixins import ExtendModelSerializers
from orders.models import Order, OrderItem


class OrderCreateSerializer(ExtendModelSerializers):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'address', 'postal_code',
            'city'
        ]


class OrderItemSerializer(ExtendModelSerializers):
    product = serializers.CharField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['product', 'order', 'price', 'quantity']
