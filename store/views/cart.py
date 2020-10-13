from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
# Create your views here.
from store.forms.checkout_form import CheckForm

from django.contrib.auth.decorators import login_required


def add_to_cart(request, slug, size):
    user = None
    if request.user.is_authenticated:
        user = request.user
    cart = request.session.get('cart')
    if cart is None:
        cart = []

    tshirt = Tshirt.objects.get(slug=slug)
    add_cart_for_anom_user(cart, size, tshirt)
    if user is not None:
        add_cart_to_database(user, size, tshirt)

    request.session['cart'] = cart
    return_url = request.GET.get('return_url')
    return redirect(return_url)


def add_cart_to_database(user, size, tshirt):
    size = SizeVariant.objects.get(size=size, tshirt=tshirt)
    existing = Cart.objects.filter(user=user, sizeVariant=size)

    if len(existing) > 0:
        obj = existing[0]
        obj.quantity = obj.quantity + 1
        obj.save()

    else:
        c = Cart()
        c.user = user
        c.sizeVariant = size
        c.quantity = 1
        c.save()


def add_cart_for_anom_user(cart, size, tshirt):
    flag = True

    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        size_short = cart_obj.get('size')
        if t_id == tshirt.id and size == size_short:
            flag = False
            cart_obj['quantity'] = cart_obj['quantity'] + 1

    if flag:
        cart_obj = {'tshirt': tshirt.id, 'size': size, 'quantity': 1}
        cart.append(cart_obj)




def cart(request):
    cart = request.session.get('cart')
    if cart is None:
        cart = []

    for c in cart:
        tshirt_id = c.get('tshirt')
        tshirt = Tshirt.objects.get(id=tshirt_id)
        c['size'] = SizeVariant.objects.get(tshirt=tshirt_id, size=c['size'])
        c['tshirt'] = tshirt

    print(cart)
    return render(request,
                  template_name='store/cart.html',
                  context={'cart': cart})

