from django.contrib import admin

from coupons.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):

    list_display = ['code', 'active', 'discount', 'valid_from', 'valid_to']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']

