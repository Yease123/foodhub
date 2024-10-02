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
    
    category = models.CharField(max_length=50)
    isveg=models.BooleanField(default=False) 
    available = models.BooleanField(default=True)
    promotion = models.CharField(max_length=100, blank=True, null=True)
    stock_level = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to="food/images/",blank=True, null=True)

    
class Usercart(models.Model):
    userid=models.ForeignKey(customeuser,on_delete=models.CASCADE)
    foodid=models.ForeignKey(Food,on_delete=models.CASCADE)
class orderedfoodbyuser(models.Model):
    orderuserid=models.ForeignKey(customeuser,on_delete=models.CASCADE)
    orderfoodid=models.ForeignKey(Food,on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    totalamount=models.IntegerField()
    totalprice=models.IntegerField()
    pickbydelivery=models.BooleanField(default=False)
    pickbyhotel=models.BooleanField(default=False)
    listedbyhotel=models.BooleanField(default=False)
    rejectbyhotel=models.BooleanField(default=False)
    addresstodeliver=models.CharField(max_length=100,null=True)
    otpfordeliveryman=models.CharField(max_length=6,null=True)
    otpforuser=models.CharField(max_length=6,null=True)
    deliverymanid=models.IntegerField(null=True)
    isdelivered=models.BooleanField(default=False)








