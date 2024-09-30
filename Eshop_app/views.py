from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.http import HttpResponse
from .forms import CategoryForm

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


# registration
def register(request):
    return render(request, 'register.html')


# user page
def user_page(request):
    return render(request, 'user_page.html')


# maso
def maso(request):
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


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catgory_list.html', {'categories': categories})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})
