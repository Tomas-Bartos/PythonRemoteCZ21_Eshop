from django import forms
from .models import Category, Product


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
