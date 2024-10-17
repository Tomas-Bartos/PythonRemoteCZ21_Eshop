from django.contrib import admin
from .models import Product, Category
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

admin.site.register(Product)


# product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


admin.site.register(Category)


# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(User, BaseUserAdmin)


class UserAdmin(BaseUserAdmin):
    # Pole, která se zobrazí v přehledu uživatelů
    list_display = (
    'username', 'email', 'first_name', 'last_name', 'address_country', 'address_city', 'is_staff', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'address_country')

    # Upravení zobrazení v detailu uživatele
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        (_('Address'), {'fields': ('address_country', 'address_city', 'address_street', 'address_zip')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Použité při přidávání nového uživatele
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'email', 'password1', 'password2', 'address_country', 'address_city', 'address_street',
            'address_zip', 'is_staff', 'is_active')}
         ),
    )
