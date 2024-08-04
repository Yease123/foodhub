from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Food(models.Model):
    foodname=models.CharField(max_length=50)
    about=models.TextField()
    price=models.IntegerField()
    resturant_name=models.ForeignKey(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="images/")
    category = models.CharField(max_length=50)
    isveg=models.BooleanField() 
    available = models.BooleanField(default=True)
    promotion = models.CharField(max_length=100, blank=True, null=True)
    stock_level = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    








