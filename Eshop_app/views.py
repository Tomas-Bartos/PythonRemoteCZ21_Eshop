from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpResponse

# Create your views here.
# request -> response
# views are request handler

from Eshop_app.models import Product


# This function will render homepage.html page
def homepage(request):
    return render(request, 'homepage.html',
                  context={
                      "all_products": Product.objects.all()
                  })


# cart
def cart(request):
    return render(request, 'cart.html')


# login
def login(request):
    return render(request, 'login.html')


# maso
def maso(request):
    # return render(request, 'maso.html',
    #               context={
    #                   "maso": Product.objects
    #               })

    # Get all products from maso category
    meat_category = get_object_or_404(Category, name='Maso')
    meat_products = Product.objects.filter(category=meat_category)

    return render(request, 'maso.html', context={
        "maso": meat_products
    })


# mlecne a chlazene
def mlecne_a_chlazene(request):
    return render(request, 'mlecne_a_chlazene.html')


# ovoce
def ovoce(request):
    return render(request, 'ovoce.html')


# mrazene
def mrazene(request):
    return render(request, 'mrazene.html')
