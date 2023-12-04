from django.contrib import admin
from .models import Cart,cart_items
# Register your models here.
admin.site.register(Cart)
admin.site.register(cart_items)