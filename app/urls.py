
from django.urls import path
from .views import home,login_user,signup_user

urlpatterns = [
       path('',home,name="home"),
       path('login/',login_user,name="login"),
       path('signup/',signup_user,name="signup")
]