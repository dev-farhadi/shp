from django.urls import path
from . import views

urlpatterns = [
    path('objects/<str:param>/', views.child_obj, name="child"),
    path('object/<int:oi>', views.object, name="object"),
    path('', views.home, name="home")
]