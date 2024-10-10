from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Přihlásí uživatele
            return redirect('user')  # Přesměrování na uzivatelskou stránku
    else:
        form = AuthenticationForm()  # Nový formulář pro GET požadavek
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')
# Create your views here.
