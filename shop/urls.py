from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:param>/',views.category, name="category"),
    path('Products/<str:param>/', views.products_type, name="child"),
    path('product/<int:oi>', views.object, name="object"),
    path('', views.home, name="home")
]