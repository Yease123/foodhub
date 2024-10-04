from django.contrib import admin
from .models import Food,customeuser,Usercart,orderedfoodbyuser,resetpassword






admin.site.register(resetpassword)

# Register your models here.
@admin.register(Usercart)
class adminusercart(admin.ModelAdmin):
    list_display=["userid","foodid"]
@admin.register(Food)
class adminfood(admin.ModelAdmin):
    list_display=[ "id","foodname","about","price","resturant_name","category" ,"isveg","available","promotion" ,"stock_level" ,"created_at" ,"updated_at" ,"photo"]
@admin.register(customeuser)
class adminuser(admin.ModelAdmin):
    list_display=[ "username","email","latitude" ,"longitude" ,"approved","isopene","address","phonenumber","created_at","updated_at" ,"isresturant","isdelivery","isuser","photo"]
    list_filter = ["approved", "isresturant", "isdelivery"] 
@admin.register(orderedfoodbyuser)
class adminorderfood(admin.ModelAdmin):
    list_display=["get_restaurant_phone","get_restaurant_name", "orderuserid",'id',"orderfoodid","ordered_at" ,"totalamount","totalprice","pickbydelivery","listedbyhotel","rejectbyhotel","addresstodeliver","otpfordeliveryman","otpforuser","deliverymanid","isdelivered",'get_delivery_name','get_delivery_number']
    list_filter = ["orderuserid", "isdelivered", "rejectbyhotel","orderfoodid__resturant_name","ordered_at",'deliverymanid'] 
    def get_restaurant_phone(self, obj):
        return obj.orderfoodid.resturant_name.phonenumber  
    get_restaurant_phone.short_description = 'Restaurant Phone' 
    def get_restaurant_name(self, obj):
        return obj.orderfoodid.resturant_name.username  
    get_restaurant_name.short_description = 'Restaurant name'
    def get_delivery_name(self, obj):
        delivery_man = customeuser.objects.get(id=obj.deliverymanid)
        return delivery_man.username 
    get_delivery_name.short_description = 'delivery man name'
    def get_delivery_number(self, obj):
        delivery_man = customeuser.objects.get(id=obj.deliverymanid)
        return delivery_man.phonenumber
    get_delivery_number.short_description = 'delivery man number'

    

     

