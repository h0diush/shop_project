from rest_framework import serializers

from common.serializers.mixins import ListModelSerializersMixin, \
    ExtendModelSerializers
from shop.models import Category, Product
from shop.serializers.products import ProductsListSerializers


class CategoriesListSerializers(ListModelSerializersMixin):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class CategoryRetrieveSerializers(ExtendModelSerializers):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'products']

    def get_products(self, obj):
        # TODO отображение ссылки
        products = Product.objects.filter(category=obj).select_related(
            'category')
        return ProductsListSerializers(products, many=True, context={
            'request': self.context['request']}).data
