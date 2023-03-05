from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    param = request.GET.get('sort')
    
    if param == 'name':
        data = Phone.objects.order_by('name')
    elif param == 'min_price':
        data = Phone.objects.order_by('price')
    elif param == 'max_price':
        data = Phone.objects.order_by('price').reverse()
    else:
        data = Phone.objects.all()

    return render(request, template, context={'phones':data})


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug)[0]
    }
    return render(request, template, context)
