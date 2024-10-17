from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


# Models are like "data plans" or "templates" that determine what data is
# stored in the database and how it is worked with.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,
                                        related_name="subcategories")

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address_country = models.CharField(max_length=100, default="")
    address_city = models.CharField(max_length=100, default="")
    address_street = models.CharField(max_length=100, default="")
    address_zip = models.CharField(max_length=20, default="")
    avatar = models.ImageField(upload_to='avatars/', default="", null=True, blank=True)


class Customer(User):
    pass


class Employee(User):
    # is_admin = models.BooleanField(default=True)
    pass


class Admin(User):
    # is_superadmin = models.BooleanField(default=True)
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='products/', blank=True, null=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Česká Lípa")
    street = models.CharField(max_length=255, default="Česká Lípa")
    city = models.CharField(max_length=100, default="Česká Lípa")
    postal_code = models.CharField(max_length=10, default="Česká Lípa")
    email = models.EmailField(default="info@info.cz")
    phone = models.CharField(max_length=20, default="Česká Lípa")
    payment_method = models.CharField(max_length=50, default="Česká Lípa")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
