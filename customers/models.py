
from django.db import models


# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=200 ,null=True)
    email=models.CharField(max_length=200 ,null=True)
    phone=models.CharField(max_length=200 ,null=True)
    location=models.CharField(max_length=200 ,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) :
        return  self.name



class Product(models.Model):
    product_name=models.CharField(max_length=200 ,null=True)
    description=models.CharField(max_length=200 ,null=True)
    price=models.IntegerField(null=True)
    size=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
   
    def __str__(self) :
        return self.product_name

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)

    STATUS=(('Pending ','Pending'),
                  ('Delivered ','Delivered') ,
                  ('Out for delivery ','Out for delivery') )

    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self) :
        return  self.product.product_name
    


#class Location(models.Model):
    #location_name=models.CharField(max_length=200,null=True)
    #date_created=models.DateTimeField(auto_created=True,null=True)
    

    

