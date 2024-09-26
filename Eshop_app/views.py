from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request -> response
# views are request handler

from Eshop_app.models import Product

# This function will render homepage.html page
def home_page(request):
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
