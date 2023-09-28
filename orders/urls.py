from django.urls import path

from orders.views import order_create, order_admin

urlpatterns = [
    path('orders/', order_create.OrderCreateView.as_view(),
         name='order_create'),
    path('admin/order/<int:order_id>/', order_admin.admin_order_detail,
         name='admin_order_detail')
]
