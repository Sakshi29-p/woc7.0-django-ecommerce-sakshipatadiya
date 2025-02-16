from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ShippingAddress

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
        return redirect('index') 

    return render(request, 'shipping_address.html')
