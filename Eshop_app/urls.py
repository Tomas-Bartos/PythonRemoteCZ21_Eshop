# views must be mapped to urls
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URL configurations. To display any URL on the running server, its address must start with Eshop_app
# for example http://127.0.0.1:8000/Eshop_app/homepage/

# path('/', views., name=''),
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('maso/', views.maso, name='maso'),
    path('ovoce/', views.ovoce, name='ovoce'),
    path('mlecne-a-chlazene/', views.mlecne_a_chlazene, name='mlecne-a-chlazene'),
    path('mrazene/', views.mrazene, name='mrazene'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)