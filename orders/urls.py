from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('process_order/', process_order, name='process_order'),
    path('me/', login_required(OrderList.as_view(), login_url='/autentication/access'), name='order_list'),
    path('<int:pk>', login_required(OrderDetail.as_view(), login_url='/autentication/access'), name='order_detail'),
]

