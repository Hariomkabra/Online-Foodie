from django.urls import path
from .views import index, all_products
from . import views 

urlpatterns = [
    path('', index, name='index'),  
    path('products/', all_products, name='all_products'),
]


