from django.contrib import admin
from restaurant import models as restaurant_model


# Register your models here.
admin.site.register(restaurant_model.Restaurant)
admin.site.register(restaurant_model.Category)
admin.site.register(restaurant_model.MenuItem)
admin.site.register(restaurant_model.Modifier)
admin.site.register(restaurant_model.Order)
admin.site.register(restaurant_model.OrderItem)
