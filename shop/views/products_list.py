from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cart.cart import Cart
from common.views.mixins import ListRetrieveViewSetMixin
from shop.models import Product
from shop.serializers.products import ProductsListSerializers, \
    ProductRetrieveSerializer, ProductAddInCartSerializers


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
        quantity = int(request.POST.get('quantity'))
        override = request.POST.get('override')
        product = self.get_object()
        if quantity:
            cart.add(
                product=product,
                quantity=quantity,
                override_quantity=override,
            )
        return Response({"message": f'{product.name} добавлен в корзину'})

    @action(
        detail=True,
        methods=['GET'],
        permission_classes=[AllowAny]
    )
    def remove_product_from_cart(self, request, slug=None):
        cart = Cart(request)
        cart.remove(self.get_object())
        return Response(
            {'message': f'{self.get_object().name} удален из корзины'})
