from django.db import models
from django.conf import settings



class Type_Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.type)

class Category_Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=255)    

    def __str__(self):
        return str(self.category)

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1080)
    category = models.ForeignKey(Category_Product, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type_Product, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return str(self.name)
    
class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Order_details(models.Model):  
    id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)  
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_details')
    quantity = models.PositiveIntegerField(default=1)
    product_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)







# Create your models here.
