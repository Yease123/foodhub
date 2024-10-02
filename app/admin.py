from django.contrib import admin
from .models import Food,customeuser,Usercart,orderedfoodbyuser,resetpassword


admin.site.register(Usercart)
admin.site.register(Food)
admin.site.register(customeuser)
admin.site.register(orderedfoodbyuser)
admin.site.register(resetpassword)

# Register your models here.
