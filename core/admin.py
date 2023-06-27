from django.contrib import admin
from .models import Product, WishList, Order

admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(Order)
