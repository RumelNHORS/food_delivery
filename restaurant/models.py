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
