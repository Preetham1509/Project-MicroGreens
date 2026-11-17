from django.db import models
from django.contrib.auth.models import User

'''class Microgreen(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_inr_2oz = models.DecimalField(max_digits=6, decimal_places=2)
    price_inr_4oz = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)

class Order(models.Model):
    STATUS_CHOICES = [
        ('REQ', 'Requested'),
        ('CON', 'Confirmed'),
        ('FUL', 'Fulfilled'),
    ]
    
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    delivery_preference = models.CharField(max_length=50) # 'Local pickup' or 'Nearby delivery'
    notes = models.TextField(blank=True)
    
    total_amount_inr = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='REQ')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    microgreen = models.ForeignKey(Microgreen, on_delete=models.PROTECT)
    size = models.CharField(max_length=10) # '2 oz' or '4 oz'
    quantity = models.IntegerField(default=1)'''

from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    delivery_preference = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    
    # This single field replaces the need for complex serializers!
    cart_data = models.JSONField(default=dict) 
    
    total_amount_inr = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='Requested')
    created_at = models.DateTimeField(auto_now_add=True)