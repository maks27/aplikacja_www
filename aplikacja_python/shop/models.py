from django.db import models
from django.utils.translation import ugettext_lazy
from django_enumfield import enum
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.


class Users(models.Model):
    user_account = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    shipment_adres = models.CharField(max_length=45, default="none")

    def __str__(self):
        return self.User.username


class Categories(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Products(models.Model):
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=350, default='brak')
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Order_products(models.Model):
    product_id = models.ManyToManyField(Products)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class StatusField(enum.Enum):
    WAIT = 0
    PAYED = 1
    SHIPMENT = 2
    END = 3

    __default__ = WAIT
    __labels__ = {
        WAIT: ugettext_lazy("Czeka na zaksiegowanie"),
        PAYED: ugettext_lazy("Opłacone"),
        SHIPMENT: ugettext_lazy("Wysłane"),
        END: ugettext_lazy("Zakończone"),

    }


class Orders(models.Model):
    order_id = models.OneToOneField(Order_products, primary_key=True, on_delete=models.CASCADE)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = enum.EnumField(StatusField)
    date = models.DateTimeField(auto_now=True)
