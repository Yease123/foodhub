
from django.urls import path
from .views import home,login_user,signup_user,logoutuser,youhotel,orderfood

urlpatterns = [
       path('',home,name="home"),
       path('login/',login_user,name="login"),
       path('signup/',signup_user,name="signup"),
       path('logout/',logoutuser,name="logout"),
        path('youhotel/',youhotel,name="youhotel"),
        path('orderfood/<int:pk>/', orderfood ,name='orderfood'),
]