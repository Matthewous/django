from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    data = Phone.objects.all()
    return render(request, template, context={'phones':data})


def show_product(request, slug):
    template = 'product.html'
    # # data = Phone.objects.filter(slug=slug)
    # context = {
    #     'phone':Phone.objects.filter(slug=slug)
    # }
    # return render(request, template, context)
    context = {
        'phone': Phone.objects.filter(slug=slug)[0]
    }
    return render(request, template, context)
