from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from cart.cart import Cart

# Create your views here.

def payment_success(request):
     return render(request,"payment_success.html",{})


@login_required
def shipping_address(request):
    if request.method == 'POST':
        shipping_full_name = request.POST.get('shipping_full_name')
        shipping_email = request.POST.get('shipping_email')
        shipping_phone_number = request.POST.get('shipping_phone_number')
        shipping_address = request.POST.get('shipping_address')
        shipping_city = request.POST.get('shipping_city')
        shipping_state = request.POST.get('shipping_state')
        shipping_zipcode = request.POST.get('shipping_zipcode')
        shipping_country = request.POST.get('shipping_country')

        # Basic validation to ensure no field is left empty
        if not all([shipping_full_name, shipping_email, shipping_phone_number, shipping_address, shipping_city, shipping_state, shipping_zipcode, shipping_country]):
            messages.error(request, 'All fields are required.')
            return redirect('shipping_address')

        # Check if user already has a shipping address and update it
        shipping_instance, created = ShippingAddress.objects.get_or_create(user=request.user)

        shipping_instance.shipping_full_name = shipping_full_name
        shipping_instance.shipping_email = shipping_email
        shipping_instance.shipping_phone_number = shipping_phone_number
        shipping_instance.shipping_address = shipping_address
        shipping_instance.shipping_city = shipping_city
        shipping_instance.shipping_state = shipping_state
        shipping_instance.shipping_zipcode = shipping_zipcode
        shipping_instance.shipping_country = shipping_country
        shipping_instance.save()

        messages.success(request, 'Shipping address updated successfully!')
        return 
        # return redirect('index') 

    return render(request, 'shipping_address.html')


@login_required(login_url='login_user')
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    cart_quantity = cart.get_quants()
    totals = cart.cart_totals()

    return render(request,'checkout.html',{'cart_products':cart_products, 'quantities':cart_quantity, 'totals':totals})


def process_order(request):
    
    if request.method == "POST":

        cart = Cart(request)
        totals = cart.cart_totals()

        # creating shipping address
        my_shipping = request.POST
        user = request.user
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        shipping_address = f"{my_shipping['shipping_address']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        amount_paid = int(totals)

        create_order = Order(user=user,email=email,full_name=full_name,shipping_address=shipping_address,amount_paid=amount_paid)
        create_order.save()


        messages.success(request, 'Order processed successfully!')
    
        return redirect('process_order')
    
    return render(request,"process_order.html",{})
