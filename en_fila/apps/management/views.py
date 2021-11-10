from django.shortcuts import render
from django.http import JsonResponse
from .models import Owner_areas
from ..mi_fila.models import *
from ..premium.models import *
# Create your views here.


def managementIndex(request):
    if request.user.is_authenticated:
        return managementpages(request)
    else:
        return render(request, "premium/login.html")


def managementpages(request):
    if request.method == "POST":
        owner = Suscribed.objects.get(suscriber=request.user)
        print(owner.id)
        for x in range(4):
            place_name = request.POST["place"+str(x)]
            try:
                owner_areas = Owner_areas.objects.get(owner=owner, area_id=x)
                owner_areas.place_name = place_name
            except Owner_areas.DoesNotExist:
                owner_areas = Owner_areas(
                    owner=owner,
                    place_name=place_name,
                    area_id=x
                )
            owner_areas.save()
    return render(request, "management/index.html")

def fila_area(request):
    return render(request, "management/filaarea.html")