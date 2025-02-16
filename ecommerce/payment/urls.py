from django.urls import path
from . import views


urlpatterns = [
    path('payment_success/',views.payment_success,name="payment_success"),
    path('shipping_address/',views.shipping_address,name="shipping_address"),
    path('checkout/',views.checkout,name="checkout"),
    path('process_order/',views.process_order,name="process_order"),
]
