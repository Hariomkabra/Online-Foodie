# cart/urls.py (or the appropriate file where your cart URLs are defined)

from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('view_cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('adjust_cart/<int:product_id>/', adjust_cart, name='adjust_cart'),  # Pass product_id as parameter
]
