from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Object, Product_list
from django.contrib.auth.decorators import login_required
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
    shop_item = Product_list.objects.filter(user_id__id=request.user.id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        userobject = Product_list(object_id_id=obj_id, quantity=quantity, user_id=request.user)
        userobject.save()
        return render(request, 'shoping.html', {'shop_item': shop_item})
    
def delete_item(request, param):
    deleted = Product_list.objects.filter(id=param).delete()
    shop_item = Product_list.objects.all()
    return render(request, 'shoping.html', {'shop_item' : shop_item})

def delete(request):
    delete = Product_list.objects.all().delete()
    return render(request, 'shoping.html')

