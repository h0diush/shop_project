from rest_framework import serializers

from common.serializers.mixins import ListModelSerializersMixin, \
    ExtendModelSerializers
from shop.models import Product


class ProductsListSerializers(ListModelSerializersMixin):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'slug', 'price', 'available', 'category'
        ]


class ProductRetrieveSerializer(ExtendModelSerializers):
    category = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2,
                                     coerce_to_string=True)

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'category', 'price', 'available', 'created'
        ]

    def get_category(self, obj):
        context = {
            'name': obj.category.name,
            'slug': obj.category.slug
        }
        return context


class ProductAddInCartSerializers(serializers.Serializer):
    quantity = serializers.CharField(max_length=2,
                                     help_text="Кол-во товара [1...20]")
    override = serializers.HiddenField(default=False, initial=False)

    def validate_quantity(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Необходимо ввести число')
        if value < 0 or value > 20:
            raise serializers.ValidationError("Проверьте диапазон. [1...20]")
        return value
