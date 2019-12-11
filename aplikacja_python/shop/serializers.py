from rest_framework import serializers

from shop.models import Users, Products, Orders, Order_products, Categories


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=45)
    last_name = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=45)
    adres = serializers.CharField(max_length=45)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.adres = validated_data.get('adres', instance.adres)
        instance.save()
        return instance


class ShopSerializer(serializers.ModelSerializer):
    class Users:
        model = Users
        fields = '__all__'

    class Products:
        model = Products
        fields = '__all__'

    class Order_products:
        model = Order_products
        fields = '__all__'

    class Orders:
        model = Orders
        fields = '__all__'

    class Categories:
        model = Categories
        fields = '__all__'
