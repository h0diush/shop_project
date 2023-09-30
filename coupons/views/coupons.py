from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coupons.models import Coupon
from coupons.serializers.coupons import CouponSerializer


class CouponView(APIView):
    # TODO сделать отображение продуктов

    def post(self, request, *args, **kwargs):
        now = timezone.now()
        serializer = CouponSerializer(data=request.POST)
        serializer.is_valid()
        code = serializer.data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now
            )
            request.session['coupon_id'] = coupon.id
            return Response({"message": f'Купон {coupon.code} принят'},
                            status=status.HTTP_200_OK)
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            return Response({"message": 'Такого купона не существует'},
                            status=status.HTTP_400_BAD_REQUEST)
