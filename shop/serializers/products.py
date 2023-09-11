from common.serializers.mixins import ExtendModelSerializers
from shop.models import Product
from rest_framework import serializers


class ProductsListSerializers(ExtendModelSerializers):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'slug', 'price', 'available'
        ]

    def get_slug(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.slug)

