# views must be mapped to urls
from django.urls import path
from . import views

# URL configurations. To display any URL on the running server, its address must start with Eshop_app
# for example http://127.0.0.1:8000/Eshop_app/base/
urlpatterns = [
    path('base/', views.base),
    path('homepage/', views.home_page, name='homepage'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
]
