from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Object, Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def home(request):
    object = Object.objects.order_by('-id')[:5]
    paginator = Paginator(object, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html' ,{'page_obj' : page_obj})


def object(request,oi):
    object = Object.objects.filter(id=oi)
    return render(request, 'object.html', {'object' : object})


def child_obj(request,param):
    object = Object.objects.filter(type__type=param)
    return render(request,'child_obj.html', {'object' : object})


@login_required
def shoping(request, obj_id):
    shop_item = Order.objects.filter(user_id__id=request.user.id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        userobject = Order(object_id_id=obj_id, quantity=quantity, user_id=request.user)
        userobject.save()
        return render(request, 'shoping.html', {'shop_item': shop_item})
    else:
        return render(request, 'shoping.html', {'shop_item': shop_item})
    

@login_required    
def shopping(request):
   shop_item = Order.objects.filter(user_id__id=request.user.id) 
   return render(request, 'shoping.html', {'shop_item': shop_item})
 


