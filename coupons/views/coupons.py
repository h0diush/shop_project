from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coupons.models import Coupon
from coupons.serializers.coupons import CouponSerializer


@extend_schema_view(
    post=extend_schema(summary='Проверка купона', tags=["Купоны"],
                       request=CouponSerializer, responses=CouponSerializer)
)
class CouponView(APIView):

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
            return Response(CouponSerializer.data,
                            status=status.HTTP_200_OK)
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            return Response({"message": 'Такого купона не существует'},
                            status=status.HTTP_400_BAD_REQUEST)
