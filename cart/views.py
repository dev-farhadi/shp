from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Object
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html',{})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        obj_id = int(request.POST.get('obj_id'))
        object = get_object_or_404(Object, id=obj_id)
        cart.add(object=object)

        response = JsonResponse({'object name': object.name})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass

