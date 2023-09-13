from cart.urls import urlpatterns as cart_url
from shop.urls import urlpatterns as products_lis_url

app_name = 'api'

urlpatterns = []

urlpatterns += products_lis_url
urlpatterns += cart_url
