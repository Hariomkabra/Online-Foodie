from django.shortcuts import render
from products.models import Product

# Views for products.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def index(request):
    return render(request, 'home/index.html')

