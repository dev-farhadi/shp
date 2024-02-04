from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:param>/',views.category, name="category"),
    path('type/<str:param>/', views.products_type, name="type"),
    path('product/<int:oi>', views.product, name="product"),
    path('', views.home, name="home")
]