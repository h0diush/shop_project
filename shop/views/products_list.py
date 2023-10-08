from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cart.cart import Cart
from common.views.mixins import ListRetrieveViewSetMixin
from shop.models import Product
from shop.serializers.products import ProductsListSerializers, \
    ProductRetrieveSerializer, ProductAddInCartSerializers


@extend_schema_view(
    list=extend_schema(summary="Список продуктов", tags=["Магазин"],
                       responses=ProductsListSerializers),
    retrieve=extend_schema(summary="Продукт", tags=["Магазин"],
                           responses=ProductRetrieveSerializer),
    add_product_in_cart=extend_schema(summary="Добавить продукт в корзину",
                                      tags=["Магазин"],
                                      request=ProductAddInCartSerializers),
    remove_product_from_cart=extend_schema(
        summary="Удалить продукт из корзины",
        tags=["Магазин"]),
)
class ProductsListView(ListRetrieveViewSetMixin):
    queryset = Product.objects.all()
    list_serializers = ProductsListSerializers
    retrieve_serializers = ProductRetrieveSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'add_product_in_cart':
            return ProductAddInCartSerializers
        return super().get_serializer_class()

    @action(
        detail=True,
        methods=['POST'],
        permission_classes=[AllowAny]
    )
    def add_product_in_cart(self, request, slug=None):
        cart = Cart(request)
        serializer = ProductAddInCartSerializers(data=request.POST)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        product = self.get_object()
        if data["quantity"]:
            cart.add(
                product=product,
                quantity=int(data["quantity"]),
                override_quantity=data["override"],
            )
        return Response({"message": f'{product.name} добавлен в корзину'},
                        status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=['GET'],
        permission_classes=[AllowAny]
    )
    def remove_product_from_cart(self, request, slug=None):
        cart = Cart(request)
        cart.remove(self.get_object())
        return Response(
            {'message': f'{self.get_object().name} удален из корзины'},
            status=status.HTTP_200_OK)
