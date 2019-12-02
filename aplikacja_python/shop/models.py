from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adres = models.CharField(max_length=45)


class Categories(models.Model):
    name = models.CharField(max_length=45)


class Products(models.Model):
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=350, default='brak')
    name = models.CharField(max_length=45)


class Order_products(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)


class Orders(models.Model):
    order_id = models.ForeignKey(Order_products, primary_key=True, on_delete=models.CASCADE)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    date = models.DateTimeField()