from rest_framework import serializers

from common.serializers.mixins import ListModelSerializersMixin, \
    ExtendModelSerializers
from shop.models import Product
from shop.utilities.utilit_serializers import getting_link


class ProductsListSerializers(ListModelSerializersMixin):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'slug', 'price', 'available', 'category'
        ]


class ProductRetrieveSerializer(ExtendModelSerializers):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'category', 'price', 'available', 'created'
        ]

    def get_category(self, obj):
        request = self.context.get('request')
        current_url = request.build_absolute_uri()
        new_path = f"/api/shop/categories/{obj.category.slug}/"
        url = getting_link(current_url, new_path)
        context = {
            'name': obj.category.name,
            'slug': url
        }
        return context
