from django.contrib import admin
from .models import Product, Category, User

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



