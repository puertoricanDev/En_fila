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


def mi_filaAPI(request):
    fila_id = request.GET.get("fila_id")
    patient = mi_fila.objects.filter(id=fila_id)

    return JsonResponse([patient.serialize()], safe=False)
