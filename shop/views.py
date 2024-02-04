from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def home(request):
    object = Product.objects.order_by('-id')[:5]
    paginator = Paginator(object, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html' ,{'page_obj' : page_obj})


def object(request,oi):
    object = Product.objects.filter(id=oi)
    return render(request, 'object.html', {'object' : object})


def products_type(request,param):
    object = Product.objects.filter(type__type=param)
    paginator = Paginator(object, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'products_type.html', {'page_obj' : page_obj})

def category(request, param):
    object = Product.objects.filter(category__category=param)
    paginator = Paginator(object, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category.html', {'page_obj' : page_obj})
 


