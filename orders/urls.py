from django.urls import path

from orders.views import order_create

urlpatterns = [
    path('orders/', order_create.OrderCreateView.as_view(),
         name='order_create')
]
