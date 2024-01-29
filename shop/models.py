from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Type_Object(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.type)

class Category_Object(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=255)    

    def __str__(self):
        return str(self.category)

class Object(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1080)
    category = models.ForeignKey(Category_Object, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type_Object, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return str(self.name)
    
class Product_list(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)




# Create your models here.
