# print('phones/views.py')
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    # print('phones/views.py - def index')
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones_objects = Phone.objects.all().order_by('price')
    else:
        phones_objects = Phone.objects.all().order_by('-price')

    context = {
        'phones': phones_objects
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phones_objects = Phone.objects.filter(slug=slug)

    if len(phones_objects) == 0:
        return index(request)

    context = {
        'phone': phones_objects[0]
    }
    return render(request, template, context)
