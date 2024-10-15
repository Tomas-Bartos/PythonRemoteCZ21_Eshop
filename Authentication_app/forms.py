from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreationForm(UserCreationForm):
    country = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)
    street = forms.CharField(max_length=100, required=True)
    zip = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
