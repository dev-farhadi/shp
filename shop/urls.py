from django.urls import path
from . import views

urlpatterns = [
    path('shoping/',views.shopping, name="shopping"),
    path('shoping/<int:obj_id>/',views.shoping, name="shoping"),
    path('Products/<str:param>/', views.child_obj, name="child"),
    path('product/<int:oi>', views.object, name="object"),
    path('', views.home, name="home")
]