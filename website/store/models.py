from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Gecontroleerd ERD met mvr. Uberts

class Customers(models.Model):
    class Meta:
        verbose_name_plural = "Customers"

    customerID = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12)
    isRegistered = models.BooleanField()

class Address(models.Model):
    class Meta:
        verbose_name_plural = "Customer addresses"
        unique_together = ('customerID', 'address')

    customerID = models.ForeignKey(Customers)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=25)
    postalcode = models.CharField(max_length=10)

class Products(models.Model):
    class Meta:
        verbose_name_plural = "Products"

    prodNum = models.IntegerField(primary_key=True)
    prodName = models.CharField(max_length=50)
    prodPrice = models.FloatField()
    prodStock = models.IntegerField()

    def __str__(self):
        return (str(self.prodNum))

class ProductDetails(models.Model):
    class Meta:
        verbose_name_plural = "Product details"

    prodNum = models.ForeignKey(Products)
    genre = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    totalPages = models.IntegerField()
    language = models.CharField(max_length=25)
    rating = models.IntegerField()
    author = models.CharField(max_length=50)
    desc = models.TextField()
    imageLink = models.CharField(max_length=100)
    pubDatum = models.CharField(max_length=30, default="1 januari, 1990")

class WishList(models.Model):
    class Meta:
        unique_together = ('custId', 'productNum')

    custId = models.ForeignKey(Customers)
    productNum = models.ForeignKey(Products)

class Orders(models.Model):
    class Meta:
        verbose_name_plural = "Orders"

    orderNum = models.IntegerField(primary_key=True)
    orderDate = models.DateField()
    orderStatus = models.CharField(max_length=15)

class OrderDetails(models.Model):
    class Meta:
        unique_together = ('orderNum', 'productNum')
        verbose_name_plural = "Order details"

    orderNum = models.ForeignKey(Orders)
    productNum = models.ForeignKey(Products)
    amount = models.IntegerField()
