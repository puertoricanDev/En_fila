from typing import NewType
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Owner_areas, Employee
from ..mi_fila.models import *
from ..premium.models import *
# Create your views here.


def managementIndex(request):
    if request.user.is_authenticated:
        owner = Suscribed.objects.get(suscriber=request.user)
        employee_list = Employee.objects.filter(fila_admin=owner).all()
        try:
            owner_areas_test = Owner_areas.objects.get(owner=owner,area_id=0)
        except Owner_areas.DoesNotExist:
            for x in range(0, owner.areas_suscribed+1):
                owner_areas = Owner_areas(
                    owner=owner,
                    place_name="Sin nombre",
                    area_id=x
                )
                owner_areas.save()
            return managementIndex(request)
        owner_areas = Owner_areas.objects.filter(owner=owner).all()
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


def loginempleado(request):
    return render(request, "management/loginempleado.html")


def areaselect(request):
    user_empleado = request.GET.get("empleado")
    user_id = request.GET.get("empleado_id")
    try:
        empleado = Employee.objects.get(
            id=user_id, employee_user=user_empleado)
        areas = Owner_areas.objects.filter(owner=empleado.fila_admin).all()
    except Employee.DoesNotExist:
        message = "Login de empleado incorrecto, favor intentarlo de nuevo."
        return render(request, "management/loginempleado.html", {
            "message": message,
        })
    return render(request, "management/areaselect.html", {
        "empleado": empleado,
        "areas": areas,
    })


def filaarea(request):
    empleado = request.GET.get("empleado")
    id_area = request.GET.get("area")
    accion = request.GET.get("accion")
    area = Owner_areas.objects.get(id=id_area)
    print(id_area)
    if accion == "next":
        area.current_position = area.current_position + 1
        try:
            patient = mi_fila.objects.get(
                posicion=area.current_position, area_id=(area.id-1), owner=area.owner)
        except mi_fila.DoesNotExist:
            area.current_position = area.current_position - 1
            patient = mi_fila.objects.get(
                posicion=area.current_position, area_id=(area.id-1), owner=area.owner)
    elif accion == "back" and area.current_position > 0:
        area.current_position = area.current_position - 1
        try:
            patient = mi_fila.objects.get(
                posicion=area.current_position, area_id=(area.id-1), owner=area.owner)
        except mi_fila.DoesNotExist:
            area.current_position = area.current_position + 1
            patient = mi_fila.objects.get(
                posicion=area.current_position, area_id=(area.id-1), owner=area.owner)
    elif accion == "current":
        try:
            patient = mi_fila.objects.get(
                posicion=area.current_position, area_id=(area.id-1), owner=area.owner)

        except mi_fila.DoesNotExist:
            patient = "No hay nadie En-Fila"
    
    area.save()
    return render(request, "management/filaarea.html", {
        "area": area,
        "patient": patient,
        "empleado": empleado,
    })


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


def front_desk(request):
    empleado = request.POST["empleado"]
    owner_id = request.POST["owner"]
    owner_areas = Owner_areas.objects.filter(owner=owner_id).all()
    return render(request, "management/frontdesk.html", {
        "owner_areas": owner_areas,
        "empleado": empleado,
        "owner_id": owner_id,
    })


def add_patient(request):
    empleado = request.POST["empleado"]
    owner_id = request.POST["owner"]
    area_id = request.POST["area_id"]
    owner_areas = Owner_areas.objects.filter(owner=owner_id).all()
    nombre = request.POST["name"+str(area_id)]
    area = owner_areas[int(area_id)].place_name
    try:
        listado = mi_fila.objects.filter(owner_id=owner_id, owner_places=area).all()
        next_posicion = max(list.posicion for list in listado)+1
        new_patient = mi_fila(owner_id=owner_id, owner_places=area,
                          persona=nombre, posicion=next_posicion, area_id=area_id)
    except mi_fila.DoesNotExist:
        new_patient = mi_fila(owner_id=owner_id, owner_places=area,
                          persona=nombre, posicion=1, area_id=area_id)
    
    new_patient.save()
    return render(request, "management/frontdesk.html", {
        "owner_areas": owner_areas,
        "empleado": empleado,
        "new_patient":new_patient,
        "owner_id":owner_id,
    })
