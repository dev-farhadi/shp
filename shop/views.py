from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Object
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