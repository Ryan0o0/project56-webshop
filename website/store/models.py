from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Gecontroleerd ERD met mvr. Uberts

class Customer(models.Model):
    customerID = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12)
    isRegistered = models.BooleanField()

class Address(models.Model):
    class Meta:
        unique_together = ('customerID', 'address')

    customerID = models.ForeignKey(Customer)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=25)
    postalcode = models.CharField(max_length=10)

class Products(models.Model):
    prodNum = models.IntegerField(primary_key=True)
    prodName = models.CharField(max_length=50)
    prodPrice = models.FloatField()
    prodStock = models.IntegerField()

class ProductDetails(models.Model):
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

class WhishList(models.Model):
    class Meta:
        unique_together = ('custId', 'productNum')

    custId = models.ForeignKey(Customer)
    productNum = models.ForeignKey(Products)

class Order(models.Model):
    orderNum = models.IntegerField(primary_key=True)
    orderDate = models.DateField()
    orderStatus = models.CharField(max_length=15)

class OrderDetails(models.Model):
    class Meta:
        unique_together = ('orderNum', 'productNum')

    orderNum = models.ForeignKey(Order)
    productNum = models.ForeignKey(Products)
    amount = models.IntegerField()


