from django.db import models


# Models are like "data plans" or "templates" that determine what data is
# stored in the database and how it is worked with.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,
                                        related_name="subcategories")

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address_country = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_street = models.CharField(max_length=100)
    address_zip = models.CharField(max_length=20)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # def get_role(self):
    # if hasattr(self, 'customer'):
    #     return 'Zákazník'
    # if hasattr(self, 'employee'):
    #     return 'Zaměstnanec'
    # elif hasattr(self, 'admin'):
    #     return 'Admin'
    # return 'Neznámá role'


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
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
