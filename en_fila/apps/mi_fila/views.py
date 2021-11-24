import decimal
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import mi_fila
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from decimal import *
from ..management.models import Owner_areas



def mi_filaAPI(request):
    patient_id = request.GET.get("fila")
    try:
        patient = mi_fila.objects.get(id= patient_id)
        area = patient.area_id

    except mi_fila.DoesNotExist:
        return JsonResponse({"message":"Id de paciente no encontrado, favor corroborar su numero e intentar de nuevo."})
    return render(request,"mi_fila/index.html", {
        "patient":patient.serialize(),
        "area":area
    })


        
    
