from django.db import models
from django.contrib.auth.models import AbstractUser


# CustomUser extends the default Django user model to include roles
class CustomUser(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


# Restaurant represents a restaurant managed by an owner.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, related_name='restaurants', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Category represents a category of menu items within a specific restaurant.
class Category(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Menue Item Model
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='menu_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name