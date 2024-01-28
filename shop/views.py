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