from django.urls import path
from . import views

urlpatterns = [
    path('shoping/payment',views.payment, name="payment"),
    path('shoping/delete',views.delete, name="delete"),
    path('shoping/delete_item/<int:param>',views.delete_item, name="delete_item"),
    path('shoping/<int:obj_id>/',views.shoping, name="shoping"),
    path('Products/<str:param>/', views.child_obj, name="child"),
    path('product/<int:oi>', views.object, name="object"),
    path('', views.home, name="home")
]