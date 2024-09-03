from django.contrib import admin
from restaurant import models as restaurant_model
# Register your models here.

admin.site.register(restaurant_model.Restaurant)
