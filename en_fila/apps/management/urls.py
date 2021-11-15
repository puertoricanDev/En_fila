from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('',views.managementIndex,name='managementIndex'),
    path('filaarea/',views.fila_area, name='filaarea'),
    path('managementpages',views.managementpages, name='managementpages')
    
]
