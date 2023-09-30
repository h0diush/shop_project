from rest_framework import serializers

from common.serializers.mixins import ExtendModelSerializers
from coupons.models import Coupon


class CouponSerializer(ExtendModelSerializers):
    class Meta:
        model = Coupon
        fields = ['code']


class OrderWithCoupon(ExtendModelSerializers):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Coupon
        fields = ['code', 'discount']
