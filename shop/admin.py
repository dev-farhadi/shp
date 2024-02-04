from django.contrib import admin
from .models import Type_Product, Category_Product, Product, Order, Order_details

admin.site.register(Product)
admin.site.register(Type_Product)
admin.site.register(Category_Product)
admin.site.register(Order)
admin.site.register(Order_details)


# Register your models here.
