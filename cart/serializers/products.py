from rest_framework import serializers

from shop.models import Product


class ProductsInCartSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'name', 'slug', 'description', 'category',
        ]
