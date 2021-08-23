from django.shortcuts import render
from .models import Product
from cart.cart import Cart

def productList (request):
    cart = Cart(request)
    products = Product.objects.all()
    return render(request,"products/list.html"
    ,{"products":products})

def HomeView(request):
    cart = Cart(request)
    products = Product.objects.all()
    return render(request,"layouts/home.html",{"products":products})
