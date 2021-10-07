from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.tv_outhttp, name='tv_outhttp'),
]
