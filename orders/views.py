

'''# PUBLIC: Customer Portal fetching available greens
class MicrogreenListView(generics.ListAPIView):
    queryset = Microgreen.objects.filter(in_stock=True)
    serializer_class = MicrogreenSerializer
    permission_classes = [permissions.AllowAny]

# PUBLIC: Customer Portal submitting an order
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

# PROTECTED: Supplier Dashboard fetching all orders
class SupplierOrderListView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser] # Restricts access to staff/superusers


import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

def customer_portal(request):
    if request.method == 'POST':
        # Vue submits the form data here
        Order.objects.create(
            customer_name=request.POST.get('name'),
            customer_email=request.POST.get('email'),
            customer_phone=request.POST.get('phone'),
            delivery_preference=request.POST.get('fulfillment'),
            notes=request.POST.get('notes'),
            cart_data=json.loads(request.POST.get('cart_data', '{}')),
            # In a real app, calculate total server-side based on cart_data
        )
        return redirect('customer_portal_success') # Reload page or show success
        
    return render(request, 'customer_portal.html')

@login_required(login_url='/admin/login/')
def supplier_dashboard(request):
    # Fetch orders from DB and pass them directly to the Vue template
    orders = Order.objects.all().order_by('-created_at')
    
    # Convert to a list of dicts so Vue can read it easily
    orders_list = list(orders.values(
        'id', 'status', 'customer_name', 'customer_email', 
        'customer_phone', 'delivery_preference', 'notes', 'cart_data', 'created_at'
    ))
    
    # We pass the JSON string directly into the template context
    context = {
        'orders_json': json.dumps(orders_list, default=str),
        'user_email': request.user.email or request.user.username
    }
    return render(request, 'supplier_dashboard.html', context)'''

import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

def customer_portal(request):
    if request.method == 'POST':
        # Vue submits the form data here
        Order.objects.create(
            customer_name=request.POST.get('name'),
            customer_email=request.POST.get('email'),
            customer_phone=request.POST.get('phone'),
            delivery_preference=request.POST.get('fulfillment'),
            notes=request.POST.get('notes'),
            cart_data=json.loads(request.POST.get('cart_data', '{}')),
        )
        return redirect('customer_portal_success') 
        
    return render(request, 'customer_portal.html')

@login_required(login_url='/admin/login/')
def supplier_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    
    orders_list = list(orders.values(
        'id', 'status', 'customer_name', 'customer_email', 
        'customer_phone', 'delivery_preference', 'notes', 'cart_data', 'created_at'
    ))
    
    context = {
        'orders_json': json.dumps(orders_list, default=str),
        'user_email': request.user.email or request.user.username
    }
    return render(request, 'supplier_dashboard.html', context)