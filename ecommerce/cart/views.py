from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from home.models import Product
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    cart_quantity = cart.get_quants
    totals = cart.cart_totals
    return render(request,'cart_summary.html',{'cart_products':cart_products, 'quantities':cart_quantity, 'totals':totals})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product,quantity=product_qty)

        cart_quantity = cart.__len__( )

        response = JsonResponse({'Qty': cart_quantity})
        messages.success(request,("The Product is added to your Cart."))

        return response
    

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        updated_prod_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id,quantity=updated_prod_qty)

        response = JsonResponse({'Qty':updated_prod_qty})
        messages.success(request,("The Product Quantity is updated."))
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        messages.success(request,("The Product is deleted from your Cart."))
        return response