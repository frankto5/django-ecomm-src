from django.shortcuts import redirect, render
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart
from django.contrib import messages

def loginWarning(request,product_id):
    if request.user.is_anonymous:
        messages.error(request, 'Debes estar conectado para agregar productos al carrito')
    return add_product(request,product_id)

@login_required(login_url='/autentication/access')
def add_product(request,product_id):
    cart=Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("productList")

@login_required(login_url='/autentication/access')
def remove_product(request,product_id):
    cart=Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product=product)
    return redirect("productList")

@login_required(login_url='/autentication/access')
def decrement_product(request,product_id):
    cart=Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("productList")

@login_required(login_url='/autentication/access')
def clear_cart(request,product_id):
    cart=Cart(request)    
    cart.clear()
    return redirect("productList")