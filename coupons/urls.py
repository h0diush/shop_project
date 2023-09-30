from django.urls import path
from coupons.views.coupons import CouponView

urlpatterns = [
    path('apply/', CouponView.as_view(), name='apply')
]
