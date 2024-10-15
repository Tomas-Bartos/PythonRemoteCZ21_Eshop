from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, User, Admin, Employee, Order
#from .model import Customer
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from Authentication_app.views import login, register
from django.db.models import Q


# Create your views here.
# request -> response
# views are request handler


# This function will render homepage.html page
def homepage(request):
    return render(request, 'homepage.html',
                  context={
                      "all_products": Product.objects.all()
                  })

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        cart = request.session.get('cart_view', {})
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': 1
            }

        request.session['cart_view'] = cart
        return redirect('cart_view')  # Přesměrování na stránku košíku
    else:
        return HttpResponseNotAllowed(['POST'])  # Zpracování neplatných metod


def cart_view(request):
    cart = request.session.get('cart_view', {})
    total_price = 0

    for item in cart.values():
        total_price += float(item['price']) * item['quantity']

    return render(request, 'cart_view.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart_view', {})
    print(f'Obsah košíku před odebráním: {cart}')
    if str(product_id) in cart:
        del cart[str(product_id)]  # Odstraní celý produkt z košíku
        print(f'Produkt {product_id} byl úspěšně odebrán z košíku.')  # Debug
    else:
        print(f'Produkt {product_id} nebyl nalezen v košíku.')  # Debug

    request.session['cart_view'] = cart
    return redirect('cart_view')


def calculate_cart_total(cart):
    total = 0
    for product_id, product_details in cart.items():
        total += float(product_details['price']) * product_details['quantity']
    return total


def complete_order(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            print(f"User: {user}, Type: {type(user)}")

            name = request.POST.get('name')
            street = request.POST.get('street')
            city = request.POST.get('city')
            postal_code = request.POST.get('postal_code')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            payment_method = request.POST.get('payment_method')

            cart = request.session.get('cart', {})

            order = Order.objects.create(
                user=user,
                name=name,
                street=street,
                city=city,
                postal_code=postal_code,
                email=email,
                phone=phone,
                payment_method=payment_method,
                total_amount=calculate_cart_total(cart),
            )

            for product_id, product_details in cart.items():
                order.products.add(product_id)

            request.session['cart'] = {}  # Clear the cart after completing the order
            return redirect('order_success')  # Redirect to a success page

    return redirect('order_success')

def order_form(request):
    user = request.user


    name = User.username if user else ''
    street = User.address_street if user else ''
    house_number = User.address_zip if user else ''
    city = User.address_city if user else ''
    postal_code = User.address_zip if user else ''
    email = User.email if user else ''

    context = {
        'name': name,
        'street': street,
        'house_number': house_number,
        'city': city,
        'postal_code': postal_code,
        'email': email,
    }

    return render(request, 'order_form.html', context)

def order_success(request):
    return render(request, 'order_success.html')


# user page
def user_page(request):
    return render(request, 'user_page.html',
                  context={
                      "products_to_edit": Product.objects.all(),
                      "categories": Category.objects.all(),
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
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    print('ID produktu:', product.id)
    print('Produkt:', product)
    if isinstance(request.user, Customer):
        return render(request, 'customer/products.html', {'product': product})

    elif isinstance(request.user, Employee):
        return render(request, 'employee/products.html', {'product': product})

    elif isinstance(request.user, Admin):
        return render(request, 'admin/products.html', {'product': product})

    return render(request, 'product_detail.html', {'product': product})


# Edit product form
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if isinstance(request.user, Employee) or isinstance(request.user, Admin):
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


# Category delete
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('user')
    return render(request, 'category_confirm_delete.html', {'category': category})


# search
def search_products(request):
    query = request.GET.get('q')  # get search request from the get parameters
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |  # search by name
            Q(description__icontains=query) |  # search by description
            Q(category__name__icontains=query)  # search by category
        )
    else:
        products = Product.objects.all()  # if not request get all products

    return render(request, 'search_results.html', {'products': products, 'query': query})
