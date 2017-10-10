from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Products)
admin.site.register(ProductDetails)
admin.site.register(Customers)
admin.site.register(Address)
admin.site.register(Orders)
admin.site.register(OrderDetails)