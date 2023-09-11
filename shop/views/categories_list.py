from rest_framework.permissions import AllowAny

from common.views.mixins import ListRetrieveViewSetMixin
from shop.models import Category
from shop.serializers.categories import CategoriesListSerializers, \
    CategoryRetrieveSerializers


class CategoryListRetrieveViewSet(ListRetrieveViewSetMixin):
    queryset = Category.objects.all()
    retrieve_serializers = CategoryRetrieveSerializers
    list_serializers = CategoriesListSerializers
    permission_classes = [AllowAny]
    lookup_field = 'slug'
