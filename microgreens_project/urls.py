from django.contrib import admin
from django.urls import path
from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.customer_portal, name='customer_portal_success'),
    path('supplier/', views.supplier_dashboard, name='supplier_dashboard'),
]