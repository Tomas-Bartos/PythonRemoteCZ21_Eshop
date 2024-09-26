from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Přihlásí uživatele
            return redirect('home')  # Přesměrování na domovskou stránku
    else:
        form = AuthenticationForm()  # Nový formulář pro GET požadavek
    return render(request, 'authentication/login.html', {'form': form})

def home(request):
    return render(request, 'home.html')
# Create your views here.
