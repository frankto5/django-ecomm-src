from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registerView.as_view(),name='register'),
    path('exit/',logoutView,name='logout'),
    path('access/',loginView,name='login'),
]
