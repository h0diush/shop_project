from api.spectacular.urls import urlpatterns as doc_url
from cart.urls import urlpatterns as cart_url
from coupons.urls import urlpatterns as coupon_url
from orders.urls import urlpatterns as orders_url
from payment.urls import urlpatterns as payment_url
from shop.urls import urlpatterns as products_list_url

app_name = 'api'

urlpatterns = []

urlpatterns += doc_url
urlpatterns += cart_url
urlpatterns += coupon_url
urlpatterns += orders_url
urlpatterns += products_list_url
urlpatterns += payment_url