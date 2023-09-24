from common.serializers.mixins import ExtendModelSerializers
from orders.models import Order


class OrderCreateSerializer(ExtendModelSerializers):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'address', 'postal_code',
            'city'
        ]
