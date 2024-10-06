from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.http import HttpResponse
from .forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
# request -> response
# views are request handler


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
    return render(request, 'user_page.html',
                  context={
                      "products_to_edit": Product.objects.all()
                  })


# maso
def maso(request):
    # Get all products from category
    maso_category = get_object_or_404(Category, id=2)
    maso_products = Product.objects.filter(category=maso_category)

    return render(request, 'maso.html', context={
        "maso": maso_products
    })


# mlecne a chlazene
def mlecne_a_chlazene(request):
    # Get all products from category
    mlecne_chlazene_category = get_object_or_404(Category, id=3)
    mlecne_chlazene_products = Product.objects.filter(category=mlecne_chlazene_category)

    return render(request, 'mlecne_a_chlazene.html', context={
        "mlecne_chlazene": mlecne_chlazene_products
    })


# ovoce
def ovoce(request):
    # Get all products from category
    ovoce_category = get_object_or_404(Category, id=1)
    ovoce_products = Product.objects.filter(category=ovoce_category)

    return render(request, 'ovoce.html', context={
        "ovoce": ovoce_products
    })


# mrazene
def mrazene(request):
    # Get all products from category
    mrazene_category = get_object_or_404(Category, id=4)
    mrazene_products = Product.objects.filter(category=mrazene_category)

    return render(request, 'mrazene.html', context={
        "mrazene": mrazene_products
    })


# product detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


# Edit product form
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # if form is POST, is validated and if correct it will be saved
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # return redirect('product_detail', pk=product.pk)  # Redirect back to product detail
            return redirect('user')  # Redirect back to user_page.html
    else:
        # form = ProductForm()
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})


# create product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user')  # Redirect back to user_page.html
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


# delete product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('user')  # redirect after delete

    return render(request, 'delete_product.html', {'product': product})

# Category create
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('category_list')
            return redirect('user')

    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


# Category list
def category_list(request):
    categories = Category.objects.all()
    print(f'Categories: {categories}')
    return render(request, 'category_list.html', {'categories': categories})


# Category update
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})
