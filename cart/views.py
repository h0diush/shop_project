from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from cart.serializers.products import ProductsInCartSerializer


class CartDetailView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        serialized_cart_data = []
        end_price: dict[str, int] = {'end_price': 0}
        for item in cart:
            product = item['product']
            product_data = ProductsInCartSerializer(product).data
            item['product'] = product_data
            serialized_cart_data.append(item)
            end_price['end_price'] += item['total_price']
        context = {'items': serialized_cart_data}
        context.update(end_price)
        return Response(context)


class CartClearView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return Response({'message': "Корзина очищена"})
