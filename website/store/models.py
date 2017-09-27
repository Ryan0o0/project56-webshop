from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Deze tabellen zijn nog niet migrated. Nog checken.

class Customer(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    email = models.CharField(max_length=100)

class Products(models.Model):
    productNum = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productRating = models.IntegerField(max_length=1)
    stock = models.IntegerField()
    productDescription = models.TextField()
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    imageLink = models.CharField(max_length=100)
    language = models.CharField(max_length=30)
    total = models.IntegerField(4)

class WhishList(models.Model):
    id = models.ForeignKey(Customer, primary_key=True)
    productNum = models.ForeignKey(Products, primary_key=True)

class Order(models.Model):
    orderNum = models.IntegerField(primary_key=True)
    id = models.ForeignKey(User, null=True)
    customerName = models.CharField(max_length=50)
    customerSurname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=75)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    totalPrice = models.FloatField()

class OrderDetails(models.Model):
    orderNum = models.ForeignKey(Order, primary_key=True)
    productNum = models.ForeignKey(Products, primary_key=True)
    amount = models.IntegerField()


