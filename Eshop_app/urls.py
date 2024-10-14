# views must be mapped to urls
from django.urls import path
from . import views
from logging import getLogger
from django.views.generic import ListView, UpdateView

# URL configurations. To display any URL on the running server, its address must start with Eshop_app
# for example http://127.0.0.1:8000/Eshop_app/homepage/
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('login/', views.login, name='login'),
    path('registrace/', views.register, name='register'),
    path('user/', views.user_page, name='user'),
    # category pages
    path('maso/', views.maso, name='maso'),
    path('ovoce/', views.ovoce, name='ovoce'),
    path('mlecne-a-chlazene/', views.mlecne_a_chlazene, name='mlecne-a-chlazene'),
    path('mrazene/', views.mrazene, name='mrazene'),
    # category manipulation
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    # product manipulation
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('edit_product', views.edit_product, name='edit_product_page'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    # search
    path('search/', views.search_products, name='search_products'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_view/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('Eshop_app/homepage/', views.homepage, name='homepage'),
    path('cart_view/complete/', views.complete_order, name='complete_order'),
    path('order/form/', views.order_form, name='order_form'),
    path('cart_view/complete/order_success', views.order_success, name='order_success'),
]
