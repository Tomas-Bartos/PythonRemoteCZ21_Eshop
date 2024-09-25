from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request -> response
# views are request handler


# This function will render base.html page
def base(request):
    return render(request, 'base.html')


# homepage
def home_page(request):
    return render(request, 'homepage.html')


# cart
def cart(request):
    return render(request, 'cart.html')


# login
def login(request):
    return render(request, 'login.html')
