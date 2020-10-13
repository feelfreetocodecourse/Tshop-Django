from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from urllib.parse import urlencode
def home(request):
    query = request.GET
    tshirts = []
    tshirts = Tshirt.objects.all()

    brand = query.get('brand')
    neckType = query.get('necktype')
    color = query.get('color')
    idealFor = query.get('idealfor')
    sleeve = query.get('sleeve')
    page = query.get('page')

    if(page is None or page == ''):
        page = 1

    if brand != '' and brand is not None:
        tshirts = tshirts.filter(brand__slug=brand)
    if neckType != '' and neckType is not None:
        tshirts = tshirts.filter(neck_type__slug=neckType)
    if color != '' and color is not None:
        tshirts = tshirts.filter(color__slug=color)
    if sleeve != '' and sleeve is not None:
        tshirts = tshirts.filter(sleeve__slug=sleeve)
    if idealFor != '' and idealFor is not None:
        tshirts = tshirts.filter(ideal_for__slug=idealFor)

    occasions = Occasion.objects.all()
    brands = Brand.objects.all()
    sleeves = Sleeve.objects.all()
    idealFor = IdealFor.objects.all()
    neckTypes = NeckType.objects.all()
    colors = Color.objects.all()

    cart = request.session.get('cart')

    paginator = Paginator(tshirts , 3)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)

    context = {
        "page_object": page_object,
        "occasions": occasions,
        "brands": brands,
        'colors': colors,
        'sleeves': sleeves,
        'neckTypes': neckTypes,
        'idealFor': idealFor, 
        'pageurl' : pageurl
    }
    return render(request, template_name='store/home.html', context=context)

