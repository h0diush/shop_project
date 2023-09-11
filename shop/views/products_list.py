from shop.models import Product
from shop.serializers.products import ProductsListSerializers
from common.views.mixins import ListViewSetMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet


class ProductsListView(ListViewSetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializers
    permission_classes = [AllowAny]
