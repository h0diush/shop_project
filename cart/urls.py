from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart_clear/', views.CartClearView.as_view(), name='cart_detail')
]
