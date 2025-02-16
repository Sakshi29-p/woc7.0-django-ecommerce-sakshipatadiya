from home.models import Product,Profile
import json

class Cart():
    def __init__(self,request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    
    def db_add(self,product,quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)

        self.session.modified = True

        # Deal with Logged in User
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # converting key '4' to "4"
            carty = json.dumps(self.cart)
            # carty = carty.replace("\'","\"")

            current_user.update(old_cart=carty)


    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)

        self.session.modified = True

        # Deal with Logged in User
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # converting key '4' to "4"
            carty = json.dumps(self.cart)
            # carty = carty.replace("\'","\"")

            current_user.update(old_cart=carty)

    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        self.cart[product_id]=product_qty

        self.session.modified = True

         # Deal with Logged in User
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # converting key '4' to "4"
            carty = json.dumps(self.cart)
            # carty = carty.replace("\'","\"")

            current_user.update(old_cart=carty)

        return self.cart
    

    def delete(self,product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True

        # Deal with Logged in User
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # converting key '4' to "4"
            carty = json.dumps(self.cart)
            # carty = carty.replace("\'","\"")

            current_user.update(old_cart=carty)
    
    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def cart_totals(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart

        total=0
        for product in products:
            if product.on_sale:
                total = total + (product.sale_price * (quantities[str(product.id)]))
            else:
                total = total + (product.price * (quantities[str(product.id)]))
        
        return total

