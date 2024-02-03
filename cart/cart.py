from shop.models import Object ,Order
from django.contrib.auth.models import User

class Cart:
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart   

    def add(self, object, quantity):
        object_id = str(object.id)
        object_quantity = str(quantity)

        if object_id in self.cart:
            pass
        else:
            self.cart[object_id] = int(object_quantity)

        self.session.modified = True     

    def remove(self, param):
        if str(param) in self.cart:
            del self.cart[str(param)]
            self.session.modified = True    

    def __len__(self):
        return len(self.cart)  

    def get_objects(self):
        objects_ids = self.cart.keys()
        objects =  Object.objects.filter(id__in=objects_ids)
        return objects
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def save_order(self,request):
       for key,value in self.cart.items():
           oi = int(key)
           object = Object.objects.get(id=oi)
           order = Order(object_id=object, user_id_id=request.user.id, quantity=value)
           order.save()
           self.session.modified = True