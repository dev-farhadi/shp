class Cart:
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart   

    def add(self, object):
        object_id = str(object.id)

        if object_id in self.cart:
            pass
        else:
            self.cart[object_id] = {'price': str(object.price)}    

        self.session.modified = True     