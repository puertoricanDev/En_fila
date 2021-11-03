"""en_fila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('homepage.urls')),
    path("management/", include('apps.management.urls')),
    path("mi_fila/", include('apps.mi_fila.urls')),
    path("premium/", include('apps.premium.urls')),
    path("tv_out/", include('apps.tv_out.urls')),
    path("ws/mi_area/", include('apps.mi_fila.routing')),
    
]
