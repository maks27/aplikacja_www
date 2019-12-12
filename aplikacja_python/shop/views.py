from shop.models import Users, Products, Orders, Order_products, Categories
from shop.serializers import UserSerializer, ProductSerializer, Order_ProductsSerializer, CategoriesSerializer, \
    OrdersSerializer
from rest_framework import viewsets, permissions, generics
from .permissions import IsAdminUserOrReadOnly


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UsersViews(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class Order_productsView(viewsets.ModelViewSet):
    queryset = Order_products.objects.all()
    serializer_class = Order_ProductsSerializer
    permission_classes = (permissions.IsAuthenticated,)
