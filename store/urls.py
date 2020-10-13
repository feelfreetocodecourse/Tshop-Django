
from django.contrib import admin
from django.urls import path
from store.views import checkout   
from store.views import validatePayment , ProductDetailView
from store.views import add_to_cart,   home, cart 
from store.views import  LoginView  , OrderListView
from store.views import signout , signup 
from django.contrib.auth.decorators import login_required
urlpatterns = [
   path('' , home , name='homepage'), 
   path('cart/' , cart), 
   path('orders/' , login_required(OrderListView.as_view() , login_url='/login/') , name='orders' ), 
   path('login/' , LoginView.as_view() , name='login'), 
   path('signup/' , signup), 
   path('logout/' , signout),
   path('checkout/' , checkout),
   path('product/<str:slug>' , ProductDetailView.as_view()) , 
   path('addtocart/<str:slug>/<str:size>' , add_to_cart) , 
   path('validate_payment' , validatePayment) 
]



