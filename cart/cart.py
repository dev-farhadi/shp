from shop.models import Object

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

    def __len__(self):
        return len(self.cart)  

    def get_objects(self):
        objects_ids = self.cart.keys()
        objects =  Object.objects.filter(id__in=objects_ids)
        return objects
    
    def get_quants(self):
        quantities = self.cart
        return quantities