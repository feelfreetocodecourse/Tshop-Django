from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from store.models import Order

class CheckForm(forms.ModelForm):
    class Meta:
        model=Order
        fields = ['shipping_address' , 'phone' , 'payment_method']