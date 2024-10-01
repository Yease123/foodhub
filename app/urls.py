
from django.urls import path
from .views import home,login_user,signup_user,logoutuser,youhotel,orderfood,addCart,removeCart

urlpatterns = [
       path('',home,name="home"),
       path('accounts/login/',login_user,name="login"),
       path('signup/',signup_user,name="signup"),
       path('logout/',logoutuser,name="logout"),
        path('youhotel/',youhotel,name="youhotel"),
        path('orderfood/<int:pk>/', orderfood ,name='orderfood'),
        path('addcart/',addCart ,name='addcart'),
          path('removecart/',removeCart ,name='removecart'),
]