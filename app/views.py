from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Food,Usercart,orderedfoodbyuser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import random
from django.db.models import Q

def generateotp():
    otp = ""
    for _ in range(6):
        digit = random.randint(0, 9)  
        otp += str(digit)  
    return otp

from .forms import signupasuser,sigupasresturant,signupasdelivery,loginvalidate,validateorder,validatedelivery,validatecustomer
User=get_user_model()
# Create your views here.
def home(request):
    cart_length=0
    foodinformation=Food.objects.all()
    if request.user.is_authenticated:
      cartinfo=Usercart.objects.filter(userid=request.user.id).values_list('foodid',flat=True) #list of tuples if not flat=true
      cart_length=cartinfo.count()
    else:
         cartinfo=Usercart.objects.all()


    context={'foodinfo':foodinformation,'cartinfo':cartinfo,'cartlength':cart_length}
    return render(request,"home.html",context)

def login_user(request):
    if request.method=="POST":
        form=loginvalidate(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,"invalid credentials")
                return render( request,'login.html',{'form':form})
                
        else:
            return render(request, "login.html", {'form': form})

    else:
         form=loginvalidate()
        
    return render(request,"login.html",{'from':form})
def signup_user(request):
    if request.method=="POST":
            identify=request.POST.get("identify")
            if identify=="user":
                form=signupasuser(request.POST)

                if form.is_valid():
                   
                    username=form.cleaned_data["username"]
                   
                    email=form.cleaned_data["email"]
                    password=form.cleaned_data["password"]
                    address=form.cleaned_data["address"]
                    phone=form.cleaned_data["phone"]
                    user=User.objects.create(username=username,email=email,address=address,phonenumber=phone,isuser=True)
                    user.set_password(password)
                    user.save()
                    
                    return redirect('login')

                else:
                     return render(request, "signup.html", {'form': form})
            #validating resturant
            elif identify=="resturant":
                form=sigupasresturant(request.POST,request.FILES)
                if form.is_valid():
                    username=form.cleaned_data["username"]
                    email=form.cleaned_data["email"]
                    password=form.cleaned_data["password"]
                    address=form.cleaned_data["address"]
                    logititude=form.cleaned_data["logititude"]
                    latitude=form.cleaned_data["logititude"]
                    phone=form.cleaned_data["phone"]
                  
                    photo=form.cleaned_data["photo"]
                  
                    user=User.objects.create(username=username,email=email,address=address,longitude=logititude,latitude=latitude,phonenumber=phone,photo=photo,isresturant=True)
                    user.set_password(password)
                    user.save()


                    return redirect("login")
                else:
                   
                    return render(request, "signup.html", {'form': form})
            elif identify=="delivery":
                form=signupasdelivery(request.POST,request.FILES)
                if form.is_valid():
                    username=form.cleaned_data["username"]
                    email=form.cleaned_data["email"]
                    password=form.cleaned_data["password"]
                    address=form.cleaned_data["address"]
                    phone=form.cleaned_data["phone"]
                    photo=form.cleaned_data["photo"]
                    user=User.objects.create(username=username,email=email,address=address,phonenumber=phone,photo=photo,isdelivery=True)
                    user.set_password(password)
                    user.save()
                    
                    return redirect("login")
                else:
                    return render(request,"signup.html",{'form':form})



                    
    else:
      form=signupasuser()
    context={'form': form}
        
           
    return render(request,"signup.html",context)
def logoutuser(request):
    logout(request)
    return redirect("home")
@login_required
def youhotel(request):
    if request.method=="POST" :
        if request.POST.get("hiddenfield")=="updatingstatus":
                
            status=request.POST.get("submitstatus")
            
            user=request.user
            userdata=User.objects.filter(email=user.email)
            if(status=='open'):
                userdata.update(isopene=True)
                return redirect("youhotel")
            if(status=='close'):
                userdata.update(isopene=False)
                return redirect("youhotel")
        elif request.POST.get("hiddenfield")=="insertingfood":
            name=request.POST.get("foodname")
            about=request.POST.get("about")
            price=request.POST.get("price")
            category=request.POST.get("category")
            stock=request.POST.get("stock")
            photo=request.FILES.get("photo")
            veg=request.POST.get("switch")
            if veg=='on':
                veg=True
            else:
                veg=False
            orderby=request.user
            fooddata=Food.objects.create(foodname=name,about=about,price=price,photo=photo,isveg=veg,stock_level=stock,category=category,resturant_name=orderby)
            fooddata.save()
    foodinformation=Food.objects.filter(resturant_name=request.user)
    context={'foodinfo':foodinformation}

    return render(request,"yourhotel.html",context)
@login_required
def orderfood(request,pk):
    fooddata=Food.objects.get(id=pk)
    context={'foodinfo':fooddata}
    if request.method=="POST":
        form=validateorder(request.POST)
        if form.is_valid():
            print("hi")
           
            totalamount=form.cleaned_data["totalamount"]
            totalprice=form.cleaned_data["totalprice"]
            address=form.cleaned_data["address"]
            
            foodinfo=orderedfoodbyuser.objects.create(orderuserid=request.user,orderfoodid=fooddata,totalamount=totalamount,totalprice=totalprice,addresstodeliver=address)
            foodinfo.save()
           
            if orderedfoodbyuser.objects.filter(orderfoodid=pk).exists():
                fooddatainfo=Food.objects.get(id=pk)
                print(fooddatainfo)
                if fooddatainfo.stock_level>=totalamount:
                    fooddatainfo.stock_level=fooddatainfo.stock_level-totalamount
                    fooddatainfo.save()
                   
                

            return redirect('orderedfood')
        else:
             print("Form errors:", form.errors)  
             context['form']=form
    else:
        form = validateorder()  
        context['form'] = form
    return render(request,"orderfood.html",context)

def addCart(request):
    userid=request.user
    foodid=request.GET.get('foodid')
    food = get_object_or_404(Food, id=foodid)
    cart=Usercart.objects.create(userid=userid,foodid=food)
    cart.save()
   
    return redirect('home')
def removeCart(request):
    userid=request.user
    foodid=request.GET.get('foodid')
    food = get_object_or_404(Food, id=foodid)
    cart=Usercart.objects.filter(userid=userid,foodid=food)
    cart.delete()
   
    return redirect('home')
def cart(request):
     cart_length=0
     if request.user.is_authenticated:
      cartinfo=Usercart.objects.filter(userid=request.user.id)
      cart_length=cartinfo.count()
      context={'cartinfo':cartinfo,'cartlength':cart_length}
      if request.method=="POST":
          cartid=request.POST.get("foodidofcart")
          userid=request.POST.get("useridofcart")
          cart=Usercart.objects.filter(userid=userid,id=cartid)
          cart.delete()
          cartinfo=Usercart.objects.filter(userid=request.user.id)
          cart_length=cartinfo.count()
          context={'cartinfo':cartinfo,'cartlength':cart_length}

          
     return render(request,'cart.html',context)
@login_required
def orderedfood(request):
    orderedfoodinfo=orderedfoodbyuser.objects.filter(orderuserid=request.user)
    
    context={"orderedfoodinfo":orderedfoodinfo}
    return render(request,'orderedfood.html',context)
@login_required
def receivedorderbyhotel(request):
    orderinfo=orderedfoodbyuser.objects.filter(orderfoodid__resturant_name__id=request.user.id)
    context={'orderinfo':orderinfo}
    if request.method=="POST":
        discard=request.POST.get("discard")
        accept=request.POST.get("accept")
        foodid=request.POST.get("foodid")
       
        if accept:
            validfood=orderedfoodbyuser.objects.get(id=foodid)
            if validfood.orderfoodid.resturant_name.id==request.user.id:
                validfood.listedbyhotel=True
                otp=generateotp()
                print(otp)
                validfood.otpfordeliveryman=otp
                validfood.save()
                return redirect("receivedorderbyhotel")

        if discard:
            validfood=orderedfoodbyuser.objects.get(id=foodid)
            if validfood.orderfoodid.resturant_name.id==request.user.id:
                validfood.rejectbyhotel=True
                validfood.save()
                updatefood=validfood.orderfoodid
                updatefood.stock_level=updatefood.stock_level+validfood.totalamount
                updatefood.save()

                return redirect("receivedorderbyhotel")
            
    return render(request,"hotelreceiveorder.html",context)
@login_required
def deliveryman(request):
    orderinfo=orderedfoodbyuser.objects.filter(listedbyhotel=True)
    context={'orderinfo':orderinfo}
    if request.method=="POST" and request.POST.get("validation")=="fordriver":
        
        form=validatedelivery(request.POST)
        if form.is_valid():
           foodid=form.cleaned_data["foodid"]
           userid=form.cleaned_data["userid"]
           orderfoodinfo=orderedfoodbyuser.objects.get(id=foodid)
           orderfoodinfo.pickbydelivery=True
           orderfoodinfo.deliverymanid=userid
           otp=generateotp()
           orderfoodinfo.otpforuser=otp
           orderfoodinfo.save()
        else:
            context['form']=form
            print("Form errors:", form.errors) 
    else:
         form = validateorder()  
         context['form'] = form
    if request.method=="POST" and request.POST.get("validation")=="forcustomer":
        form=validatecustomer(request.POST)
        if form.is_valid():
           foodid=form.cleaned_data["foodid"]
           userid=form.cleaned_data["userid"]
           orderfoodinfo=orderedfoodbyuser.objects.get(id=foodid)
           orderfoodinfo.isdelivered=True
           orderfoodinfo.save()
        else:
            context['form']=form
            print("Form errors:", form.errors) 
    else:
         form = validateorder()  
         context['form'] = form
    return render(request,"delivery.html",context)
def customehome(request,value):
    cart_length=0
    print(value)
    foodinformation=Food.objects.filter(Q(foodname__icontains=value) | Q(about__icontains=value))
    if request.user.is_authenticated:
      cartinfo=Usercart.objects.filter(userid=request.user.id).values_list('foodid',flat=True) #list of tuples if not flat=true
      cart_length=cartinfo.count()
    else:
         cartinfo=Usercart.objects.all()
    context={'foodinfo':foodinformation,'cartinfo':cartinfo,'cartlength':cart_length}
    return render(request,"home.html",context)