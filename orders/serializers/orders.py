from common.serializers.mixins import ExtendModelSerializers
from orders.models import Order, OrderItem
from shop.serializers.products import ProductRetrieveSerializer


class OrderCreateSerializer(ExtendModelSerializers):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'address', 'postal_code',
            'city'
        ]


class OrderItemSerializer(ExtendModelSerializers):
    product = ProductRetrieveSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'order', 'price', 'quantity']
