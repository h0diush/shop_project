from decimal import Decimal

import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order, OrderItem
from orders.serializers.orders import OrderItemSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


@api_view(['GET'])
def payment_completed(request):
    return Response({"message": "Оплата прошла успешно"},
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def payment_canceled(request):
    return Response({"message": "Оплата прошла успешно"},
                    status=status.HTTP_402_PAYMENT_REQUIRED)


class PaymentProcessView(APIView):

    def _get_order(self, request):
        order_id = request.session.get('order_id', None)
        order = get_object_or_404(Order, id=order_id)
        return order

    def get(self, request, *args, **kwargs):
        order = self._get_order(request)
        order_items = OrderItem.objects.filter(order=order)
        data = {}
        data.update(
            {"product": OrderItemSerializer(order_items, many=True).data})
        return Response(data)

    def post(self, request, *args, **kwargs):
        order = self._get_order(request)
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': settings.SITE_URL + 'api/completed/',
            'cancel_url': settings.SITE_URL + 'api/canceled/',
            'line_items': []
        }
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal(100)),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name
                    },
                },
                'quantity': item.quantity
            })
            if order.coupon:
                stripe_coupon = stripe.Coupon.create(
                    name=order.coupon.code,
                    percent_off=order.discount,
                    duration='once'
                )
                session_data['discounts'] = [{
                    'coupon': stripe_coupon.id
                }]
        session = stripe.checkout.Session.create(**session_data)
        return Response({'url': session.url}, status=status.HTTP_303_SEE_OTHER)
        # return redirect(session.url, code=303)

# TODO после оплаты что делать с заказом
