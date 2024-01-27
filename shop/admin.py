from django.contrib import admin
from .models import Type_Object, Category_Object, Object

admin.site.register(Object)
admin.site.register(Type_Object)
admin.site.register(Category_Object)

# Register your models here.
