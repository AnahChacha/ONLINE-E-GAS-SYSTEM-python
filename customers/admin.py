from itertools import product
from django.contrib import admin
from .models import Customer, Order,Product


# Register yo ur models here
admin.site.register([Customer,Product,Order])


