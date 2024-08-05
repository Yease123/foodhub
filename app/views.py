from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

from .forms import signupasuser,sigupasresturant,signupasdelivery,loginvalidate

# Create your views here.
def home(request):
    return render(request,"home.html")

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
                    opening=form.cleaned_data["opening"]
                    closing=form.cleaned_data["closing"]
                    photo=form.cleaned_data["photo"]
                    opening_hour={"morning":opening,"night":closing}
                    user=User.objects.create(username=username,email=email,address=address,longitude=logititude,latitude=latitude,phonenumber=phone,photo=photo,opening_hour=opening_hour,isresturant=True)
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