from decimal import Decimal

import stripe
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order, OrderItem
from orders.serializers.orders import OrderItemSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class PaymentProcessView(APIView):

    def _get_order(self, request):
        order_id = request.session.get('order_id', None)
        order = get_object_or_404(Order, id=order_id)
        return order

    def get(self, request, *args, **kwargs):
        order = self._get_order(request)
        order_item = get_object_or_404(OrderItem, order=order)
        return Response(OrderItemSerializer(order_item).data)

    def post(self, request, *args, **kwargs):
        order = self._get_order(request)
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': settings.SITE_URL + '?success=true',
            'cancel_url': settings.SITE_URL + '?canceled=true',
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
        session = stripe.checkout.Session.create(**session_data)
        # return Response(f'{session.url}')
        return redirect(session.url, code=303)

# TODO после оплаты что делать с заказом
