from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="subcategories")

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image_url = models.URLField(default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

