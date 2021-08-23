from django.urls import path
from products.views import  productList 


urlpatterns= [
    path('',productList,name='productList')
]