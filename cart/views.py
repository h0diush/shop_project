from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from common.views.mixins import CartDetailMixin


class CartDetailView(CartDetailMixin):
    pass


class CartClearView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return Response({'message': "Корзина очищена"},
                        status=status.HTTP_200_OK)
