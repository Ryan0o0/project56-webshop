from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Deze tabellen zijn nog niet migrated. Nog checken.

class Customer(models.Model):
    custId = models.ForeignKey(User, primary_key=True)
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
    type = models.CharField(max_length=20)

class WhishList(models.Model):
    class Meta:
        unique_together = ('custId', 'productNum')

    custId = models.ForeignKey(Customer)
    productNum = models.ForeignKey(Products)

class Order(models.Model):
    orderNum = models.IntegerField(primary_key=True)
    custId = models.ForeignKey(User, null=True)
    customerName = models.CharField(max_length=50)
    customerSurname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=75)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    totalPrice = models.FloatField()

class OrderDetails(models.Model):
    class Meta:
        unique_together = ('orderNum', 'productNum')

    orderNum = models.ForeignKey(Order)
    productNum = models.ForeignKey(Products)
    amount = models.IntegerField()


