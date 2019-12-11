from django.urls import path, include
from shop import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductsView)
router.register('users', views.UsersView)
router.register('categories', views.CategoriesView)
router.register('order', views.OrdersView)
router.register('OrderProducts', views.Order_productsView)
urlpatterns = [
    path('', include(router.urls)),
]
