from django.contrib import admin
from . models import Product,CustomUser,CartItem

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(CartItem)
