from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name = models.CharField(max_length=255,blank=False)
    shipping_email = models.EmailField(max_length=255,blank=False)
    shipping_phone_number = models.CharField(max_length=20,blank=False)
    shipping_address = models.CharField(max_length=555,blank=False)
    shipping_city = models.CharField(max_length=255,blank=False)
    shipping_state = models.CharField(max_length=255,blank=False)
    shipping_zipcode = models.CharField(max_length=255,blank=False)
    shipping_country = models.CharField(max_length=255,blank=False)
    
    class Meta:
        verbose_name_plural = "Shipping Address"
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'