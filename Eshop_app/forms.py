from django import forms
from .models import Category, Product, User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # editable fields
        fields = ['name', 'description', 'image', 'category', 'price']
        # fields = '__all__'


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'address_country',
                  'address_city', 'address_street', 'address_number', 'address_zip']  # Add fields as needed
        labels = {
            'username': 'Uživatelské jméno',
            'email': 'E-mail',
            'password': 'Heslo',
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'address_country': 'Země',
            'address_city': 'Město',
            'address_street': 'Ulice',
            'address_number': 'Číslo popisné',
            'address_zip': 'PSČ'
        }
        # help_texts = {
        #     'username': None,  # Removing the default username label
        # }
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'address_country': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address_city': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address_street': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address_zip': forms.TextInput(attrs={'class': 'form-control'}),
        # }
