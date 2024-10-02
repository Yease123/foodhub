
from django.urls import path
from .views import home,login_user,signup_user,logoutuser,youhotel,orderfood,addCart,removeCart,cart,orderedfood,receivedorderbyhotel,deliveryman,customehome

urlpatterns = [
       path('',home,name="home"),
       path('accounts/login/',login_user,name="login"),
       path('signup/',signup_user,name="signup"),
       path('logout/',logoutuser,name="logout"),
       path('youhotel/',youhotel,name="youhotel"),
       path('orderfood/<int:pk>/', orderfood ,name='orderfood'),
       path('addcart/',addCart ,name='addcart'),
       path('removecart/',removeCart ,name='removecart'),
       path('cart/',cart ,name='cart'),
       path('orderedfood/',orderedfood ,name='orderedfood'),
       path('receivedorderbyhotel/',receivedorderbyhotel ,name='receivedorderbyhotel'),
        path('deliveryman/',deliveryman ,name='deliveryman'),
         path('home/<str:value>/',customehome ,name='customehome'),
        
]