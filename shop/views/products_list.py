from rest_framework.permissions import AllowAny

from common.views.mixins import ListRetrieveViewSetMixin
from shop.models import Product
from shop.serializers.products import ProductsListSerializers, \
    ProductRetrieveSerializer


class ProductsListView(ListRetrieveViewSetMixin):
    queryset = Product.objects.all()
    list_serializers = ProductsListSerializers
    retrieve_serializers = ProductRetrieveSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
