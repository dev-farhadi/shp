from shop.models import Product ,Order, Order_details
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
        objects =  Product.objects.filter(id__in=objects_ids)
        return objects
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def save_order(self,request):
       order = Order(user_id_id=request.user.id)
       order.save()
       for key,value in self.cart.items():
           order_id = Order.objects.latest('id')
           oi = int(key)
           product = Product.objects.get(id=oi)
           order_details = Order_details(order_id=order_id, user_id_id=request.user.id, product_id=product, quantity=value, product_price=product.price)
           order_details.save()
           #order = Order(object_id=object, user_id_id=request.user.id, quantity=value)
          # order.save()
           self.session.modified = True