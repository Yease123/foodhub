from django.contrib import admin
from .models import Food,customeuser,Usercart,orderedfoodbyuser


admin.site.register(Usercart)
admin.site.register(Food)
admin.site.register(customeuser)
admin.site.register(orderedfoodbyuser)

# Register your models here.
