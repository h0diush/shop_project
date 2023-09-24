from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from cart.cart import Cart
from cart.serializers.products import ProductsInCartSerializer


class ExtendGeneralViewSet(GenericViewSet):
    pass


class ListRetrieveViewSetMixin(ExtendGeneralViewSet, mixins.ListModelMixin,
                               mixins.RetrieveModelMixin):
    list_serializers = None
    retrieve_serializers = None

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializers
        if self.action == 'retrieve':
            return self.retrieve_serializers
        super().get_serializer_class()


class CartDetailMixin(APIView):
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
        return Response(context, status=status.HTTP_200_OK)
