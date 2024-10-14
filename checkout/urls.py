# checkout/urls.py (or the appropriate file where your checkout URLs are defined)

from django.urls import path  
from .views import checkout
from.import views

urlpatterns = [
    path('checkout/', checkout, name='checkout'),  
     path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
