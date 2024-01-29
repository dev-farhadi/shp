from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Object, Object_User
from django.contrib.auth.decorators import login_required
from .forms import AddToCartForm
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
    shop_item = Object_User.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            userobject = Object_User(object_id=obj_id, quantity=quantity, user_id=request.user.id)
            userobject.save()
        return render(request, 'shoping.html', {'shop_item': shop_item})
