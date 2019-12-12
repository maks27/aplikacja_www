from rest_framework import serializers

from shop.models import Users, Products, Orders, Order_products, Categories


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Users
        fields = ['id', 'url', 'user_account', 'owner', 'shipment_adres']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'url', 'name']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class Order_ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_products
        fields = ['id', 'url', 'product_id', 'price']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'url', 'categories_id', 'price', 'description', 'name']
