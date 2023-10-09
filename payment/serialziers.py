from rest_framework import serializers

from common.serializers.mixins import ExtendModelSerializers
from orders.models import Order
from shop.serializers.products import ResponseProductSerializer


class ResponseUrlSerializer(serializers.Serializer):
    url = serializers.SlugField()


class ResponseProductInfoSerializer(ExtendModelSerializers):
    products = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'last_name', 'first_name', 'email', 'address', 'city',
            'postal_code', 'products', 'quantity', 'discount', 'total_price'
        ]

    @staticmethod
    def get_products(obj):
        products = []
        for item in obj.items.all():
            products.append(ResponseProductSerializer(item.product).data)
        return products

    @staticmethod
    def get_total_price(obj):
        return obj.get_total_cost()

    @staticmethod
    def get_quantity(obj):
        for item in obj.items.all():
            quantity = item.quantity
        return quantity
