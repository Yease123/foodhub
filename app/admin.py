from django.contrib import admin
from .models import Food,customeuser,Usercart


admin.site.register(Usercart)
admin.site.register(Food)
admin.site.register(customeuser)

# Register your models here.
