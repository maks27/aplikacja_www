from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adres = models.CharField(max_length=45)


class Orders(models.Model):
    order_id = models.ForeignKey
    users_id = models.ForeignKey
    """status = models."""
    date = models.DateTimeField()


class Order_products(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey
    price = models.IntegerField


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    categories_id = models.ForeignKey
    price = models.IntegerField
    description = models.TextField
    name = models.CharField(max_length=45)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
