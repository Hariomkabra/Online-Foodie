"""
URL configuration for Food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from acounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from acounts.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),  
    path('accounts/', include(urls_accounts)),
    path('products/', include(urls_products)),
    path('cart/', include(urls_cart)),
    path('checkout/', include(urls_checkout)),
   
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
