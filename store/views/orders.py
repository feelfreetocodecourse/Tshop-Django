from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
# Create your views here.
from store.forms.checkout_form import CheckForm


from django.views.generic.list import ListView



class OrderListView(ListView):
    template_name = 'store/orders.html'
    model = Order
    paginate_by = 5
    context_object_name = 'orders'

    def get_queryset(self):
        return  Order.objects.filter(user = self.request.user).order_by('-date').exclude(
        order_status='PENDING')
