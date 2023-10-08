from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.response import Response

from cart.cart import Cart
from common.views.mixins import CartDetailMixin
from orders.models import OrderItem
from orders.serializers.orders import OrderCreateSerializer
from orders.tasks import order_created


@extend_schema_view(
    get=extend_schema(summary='Получить заказ', tags=["Заказы"]),
    post=extend_schema(summary='Создать заказ', tags=["Заказы"])
)
class OrderCreateView(CartDetailMixin):

    @extend_schema(
        request=OrderCreateSerializer,
        responses={201: OrderCreateSerializer.data},
        methods=["POST"]
    )
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount
            order.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        order_created.delay(order.id)  # Отправка писем о совершении покупок
        request.session['order_id'] = order.id
        return Response(serializer.data, status=status.HTTP_201_CREATED)
