from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import products_list

router = DefaultRouter()
router.register('', products_list.ProductsListView, 'products_list')

urlpatterns = [
    path('products/', include(router.urls)),
]

# urlpatterns += path('products/', include(router.urls))
