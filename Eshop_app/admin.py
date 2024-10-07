from django.contrib import admin
from .models import Product, Category


admin.site.register(Product)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')