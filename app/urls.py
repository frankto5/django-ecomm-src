from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from products.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('autentication/',include("autenticacion.urls")),
    path('products/',include("products.urls")),
    path('cart/',include("cart.urls")),
    path('orders/',include("orders.urls")),
    path('',HomeView,name='HomeView'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
