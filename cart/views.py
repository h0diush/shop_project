from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from common.views.mixins import CartDetailMixin


@extend_schema_view(
    get=extend_schema(summary='Корзина', tags=["Магазин"])
)
class CartDetailView(CartDetailMixin):
    pass


@extend_schema_view(
    get=extend_schema(summary='Очистить корзину', tags=["Магазин"])
)
class CartClearView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return Response({'message': "Корзина очищена"},
                        status=status.HTTP_200_OK)
