from django.shortcuts import render
from django.http import JsonResponse
from .models import Owner_areas, Employee
from ..mi_fila.models import *
from ..premium.models import *
# Create your views here.


def managementIndex(request):
    if request.user.is_authenticated:
        owner = Suscribed.objects.get(suscriber=request.user)
        try:
            owner_areas = Owner_areas.objects.filter(owner=owner).all()
        except Owner_areas.DoesNotExist:
            return render(request, "management/index.html")
        employee_list = Employee.objects.filter(fila_admin=owner).all()
        return render(request, "management/index.html", {
            "employee_list": employee_list,
            "owner_areas": owner_areas,
        })

    else:
        return render(request, "premium/login.html")


def managementpages(request):
    if request.method == "POST":
        owner = Suscribed.objects.get(suscriber=request.user)
        for x in range(0, owner.areas_suscribed+1):
            place_name = request.POST["place"+str(x)]
            print(place_name)
            try:
                owner_areas = Owner_areas.objects.get(owner=owner, area_id=x)
                if place_name != "":
                    owner_areas.place_name = place_name
                    owner_areas.save()
            except Owner_areas.DoesNotExist:
                owner_areas = Owner_areas(
                    owner=owner,
                    place_name=place_name,
                    area_id=x
                )
                owner_areas.save()

        return managementIndex(request)


def fila_area(request):
    return render(request, "management/filaarea.html")


def create_employee(request):
    if request.method == "POST":
        fila_employee = request.POST['fila_employee']
        employee_user = request.POST['employee_user']
        owner = Suscribed.objects.get(suscriber=request.user)
        new_employee = Employee(
            fila_admin=owner, fila_employee=fila_employee, employee_user=employee_user)
        new_employee.save()

    return managementIndex(request)

def delete_employee(request):
    if request.method == "POST":
        employee_id = request.POST['employee_list']
        employee = Employee.objects.filter(id=employee_id)
        employee.delete()
    return managementIndex(request)
