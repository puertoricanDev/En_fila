from django.shortcuts import render
from django.http import JsonResponse
from en_fila.apps.management.models import Owner_areas
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
        owner = request.user
        
        for x in range(4):
            owner_areas = Owner_areas.objects.get(owner = owner,place_id = x)
            if Owner_areas.DoesNotExist:
                place_name = request.POST["place"+x]
                owner_areas = Owner_areas(
                        owner = owner,
                        place_name = place_name,
                        places_id = x
                    )
            else:
                owner_areas.place_name = place_name
            owner_areas.save()
    else:
        return JsonResponse({"error": "POST request required."}, status=400)
    return render(request, "management/index.html")
