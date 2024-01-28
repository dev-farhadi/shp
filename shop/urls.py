from django.urls import path
from . import views

urlpatterns = [
    path('shoping/<int:obj_id>/',views.shoping, name="shoping"),
    path('objects/<str:param>/', views.child_obj, name="child"),
    path('object/<int:oi>', views.object, name="object"),
    path('', views.home, name="home")
]