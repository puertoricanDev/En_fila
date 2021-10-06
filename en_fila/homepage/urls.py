from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('', views.index, name='index'),

]