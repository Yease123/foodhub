from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class customeuser(AbstractUser):
   
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    approved=models.BooleanField(default=False)
    isopene=models.BooleanField(default=True)
    address=models.TextField(blank=True, null=True)
    phonenumber=models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    isresturant=models.BooleanField(blank=True, null=True,default=False)
    isdelivery=models.BooleanField(blank=True, null=True,default=False)
    isuser=models.BooleanField(blank=True, null=True,default=False)
    photo=models.ImageField(upload_to="user/images/",blank=True, null=True)


class Food(models.Model):
    foodname=models.CharField(max_length=50)
    about=models.TextField()
    price=models.IntegerField()
    resturant_name=models.ForeignKey(customeuser,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="images/")
    category = models.CharField(max_length=50)
    isveg=models.BooleanField() 
    available = models.BooleanField(default=True)
    promotion = models.CharField(max_length=100, blank=True, null=True)
    stock_level = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to="food/images/",blank=True, null=True)

    








