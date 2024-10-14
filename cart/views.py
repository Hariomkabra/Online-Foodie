from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product  # Assuming you have a Product model

# View to display the cart page
def view_cart(request):
    """A view that renders the cart contents page"""
    cart = request.session.get('cart', {})  # Get the cart from the session
    cart_items = []
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity
        })
    
    total = sum(item['total_price'] for item in cart_items)  # Calculate total price
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

# View to add a product to the cart
def add_to_cart(request, product_id):
    """Add a product to the cart"""
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Get the quantity from the POST request
    
    cart = request.session.get('cart', {})  # Get the cart from the session, or create a new one

    if str(product_id) in cart:
        cart[str(product_id)] += quantity  # If the product is already in the cart, update the quantity
    else:
        cart[str(product_id)] = quantity  # Add the new product to the cart
    
    request.session['cart'] = cart  # Save the cart back to the session
    return redirect('view_cart')  # Redirect to the cart page

# View to adjust the quantity of items in the cart
def adjust_cart(request, product_id):
    """Adjust the quantity of the specified product in the cart"""
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 0))  # Get the new quantity from the form
    
    if quantity > 0:
        cart[str(product_id)] = quantity  # Update the quantity in the cart
    else:
        cart.pop(str(product_id), None)  # If the quantity is 0, remove the product from the cart
    
    request.session['cart'] = cart  # Save the updated cart to the session
    return redirect('view_cart')
