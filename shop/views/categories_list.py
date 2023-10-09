from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import AllowAny

from common.views.mixins import ListRetrieveViewSetMixin
from shop.models import Category
from shop.serializers.categories import CategoriesListSerializers, \
    CategoryRetrieveSerializers


@extend_schema_view(
    list=extend_schema(summary="Список категорий", tags=["Магазин"],
                       responses=CategoriesListSerializers),
    retrieve=extend_schema(summary="Категория", tags=["Магазин"],
                           responses=CategoryRetrieveSerializers),
)
class CategoryListRetrieveViewSet(ListRetrieveViewSetMixin):
    queryset = Category.objects.all()
    retrieve_serializers = CategoryRetrieveSerializers
    list_serializers = CategoriesListSerializers
    permission_classes = [AllowAny]
    lookup_field = 'slug'
