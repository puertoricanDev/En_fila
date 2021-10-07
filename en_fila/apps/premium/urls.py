from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.premiumUsr, name='premiumUsr'),
    path('login/',views.login_view, name='login'),
    path('registe', views.register, name='register'),
    
]
