from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import products_list, categories_list

router = DefaultRouter()
router.register('products', products_list.ProductsListView, 'products_list')
router.register('categories', categories_list.CategoryListRetrieveViewSet,
                'categories_list')

urlpatterns = []

urlpatterns += path('shop/', include(router.urls)),
