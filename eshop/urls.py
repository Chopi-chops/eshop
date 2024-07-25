"""
URL configuration for eshop project.

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
from django.contrib import admin
from django.urls import path
from django.conf import settings  # 1
from django.conf.urls.static import static  # 2
from core.views import *
from costumerapp.views import *
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('search/', search),
    path('product/<int:id>/', product_detail, name='product-detail'),
    path('product-create/', product_create, name='product-create'),
    path('user-create/', user_create, name='user-create'),
    path('users/', users_list),
    path('user/<int:id>/', user_cabinet, name='user-cabinet'),
    path('costumers/', costumer_view),
    path('costumer-create/', costumer_create, name='costumer-create'),
    path('news/', news_view),
    path('new/<int:id>/', new_detail, name='new-detail'),
    path('new-create/', new_create, name='new-create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 3

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
