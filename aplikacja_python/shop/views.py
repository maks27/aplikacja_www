from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from shop.models import Users, Products, Orders, Order_products, Categories
from shop.serializers import UserSerializer, ProductSerializer, Order_ProductsSerializer, CategoriesSerializer, \
    OrdersSerializer
from rest_framework import viewsets
from django.shortcuts import render


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class Order_productsView(viewsets.ModelViewSet):
    queryset = Order_products.objects.all()
    serializer_class = Order_ProductsSerializer
