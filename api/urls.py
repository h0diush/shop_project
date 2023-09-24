from cart.urls import urlpatterns as cart_url
from orders.urls import urlpatterns as orders_url
from shop.urls import urlpatterns as products_list_url

app_name = 'api'

urlpatterns = []

urlpatterns += cart_url
urlpatterns += orders_url
urlpatterns += products_list_url
