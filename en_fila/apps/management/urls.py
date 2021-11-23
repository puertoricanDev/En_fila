from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('',views.managementIndex,name='managementIndex'),
    path('filaarea/',views.filaarea, name='filaarea'),
    path('managementpages/',views.managementpages, name='managementpages'),
    path('createemployee/',views.create_employee,name='create_employee'),
    path('deleteemployee/', views.delete_employee, name='delete_employee'),
    path('areaselect/',views.areaselect, name="areaselect"),
    path('loginempleado/', views.loginempleado, name="loginempleado"),
    path('frontdesk',views.front_desk, name="frontdesk"),
   
]
