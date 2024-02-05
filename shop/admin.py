from typing import Any
from django.contrib import admin
from .models import Type_Product, Category_Product, Product, Order, Order_details, Product_prices


class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Any, form: Any, change: Any):

        product_prices = Product_prices()
        product_prices.product_id = obj
        product_prices.product_price = obj.price

        product_prices.save()
        return super().save_model(request, obj, form, change)

    
    
admin.site.register(Product, ProductAdmin)


admin.site.register(Type_Product)
admin.site.register(Category_Product)
admin.site.register(Order)
admin.site.register(Order_details)
admin.site.register(Product_prices)


# Register your models here.
