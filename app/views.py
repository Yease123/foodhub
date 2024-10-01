from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Food,Usercart
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


from .forms import signupasuser,sigupasresturant,signupasdelivery,loginvalidate
User=get_user_model()
# Create your views here.
def home(request):
    foodinformation=Food.objects.all()
    if request.user:
      cartinfo=Usercart.objects.filter(userid=request.user.id).values_list('foodid',flat=True)
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