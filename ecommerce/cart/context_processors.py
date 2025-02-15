from .cart import Cart

# create context processors so our can work on all pages

def cart(request):
    return {'cart':Cart(request)}