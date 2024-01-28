from django.db import models


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



# Create your models here.
