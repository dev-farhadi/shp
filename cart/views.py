from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Object
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def cart_summary(request):
    cart =Cart(request)
    cart_objects = cart.get_objects()
    cart_quantity = cart.get_quants()
    return render(request, 'cart_summary.html',{'cart_objects' : cart_objects, 'cart_quantity' : cart_quantity})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        obj_id = int(request.POST.get('obj_id'))
        obj_qty = int(request.POST.get('obj_qty'))

        object = get_object_or_404(Object, id=obj_id)
        cart.add(object=object, quantity=obj_qty)

        cart_quantiy = cart.__len__()
        response = JsonResponse({'qty' : cart_quantiy})
        return response


def cart_delete(request, param):
    cart = Cart(request)
    cart.remove(param)
    return redirect('cart_summary')

def cart_update(request):
    pass

