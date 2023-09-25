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


class CartDetailMixin(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        serialized_cart_data = []
        for item in cart:
            product = item['product']
            product_data = ProductsInCartSerializer(product).data
            item['product'] = product_data
            serialized_cart_data.append(item)
        context = {'items': serialized_cart_data}
        return Response(context, status=status.HTTP_200_OK)
