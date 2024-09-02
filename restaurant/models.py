from django.db import models
from django.contrib.auth.models import AbstractUser


# CustomUser extends the default Django user model to include roles
class CustomUser(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)



