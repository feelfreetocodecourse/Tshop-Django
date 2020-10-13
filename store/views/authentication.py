from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from store.forms import  CheckForm , CustomerCreationForm , CustomerAuthForm
from django.views.generic.base import View

class LoginView(View):  
    def get(self , request):
        form = CustomerAuthForm()
        print('LOGIN VIEW CLASS')
        next_page = request.GET.get('next')
        if next_page is not None:
            request.session['next_page'] = next_page
        return render(request,
                      template_name='store/login.html',
                      context={'form': form})

    def post(self , request):
        form = CustomerAuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                loginUser(request, user)

                session_cart = request.session.get('cart')
                if session_cart is None:
                    session_cart = []
                else:
                    for c in session_cart:
                        size = c.get('size')
                        tshirt_id = c.get('tshirt')
                        quantity = c.get('quantity')
                        cart_obj = Cart()
                        cart_obj.sizeVariant = SizeVariant.objects.get(
                            size=size, tshirt=tshirt_id)
                        cart_obj.quantity = quantity
                        cart_obj.user = user
                        cart_obj.save()

                # { size , tshirt , quantiti }
                cart = Cart.objects.filter(user=user)
                session_cart = []
                for c in cart:
                    obj = {
                        'size': c.sizeVariant.size,
                        'tshirt': c.sizeVariant.tshirt.id,
                        'quantity': c.quantity
                    }
                    session_cart.append(obj)

                request.session['cart'] = session_cart
                next_page = request.session.get('next_page')
                if next_page is None:
                    next_page = 'homepage'
                return redirect(next_page)
        else:
            return render(request,
                          template_name='store/login.html',
                          context={'form': form})



def signup(request):
    if (request.method == 'GET'):
        form = CustomerCreationForm()
        context = {"form": form}
        return render(request,
                      template_name='store/signup.html',
                      context=context)

    else:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            print(user)
            return redirect('login')
        context = {"form": form}
        return render(request,
                      template_name='store/signup.html',
                      context=context)


def signout(request):
    logout(request)
    return render(request, template_name='store/home.html')
