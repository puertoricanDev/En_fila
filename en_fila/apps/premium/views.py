import decimal
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Suscribed, User
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from decimal import *


def premiumUsr(request):
    return JsonResponse(["name:'Random user', access: 'True'"], safe=False)


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        business_name = request.POST["business_name"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "premium/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "premium/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        try:
            suscribed = Suscribed(suscriber=user,business_name=business_name)
            suscribed.save()
        except IntegrityError:
            return render(request, "premium/register.html", {
                "message": "Can not suscribe user."
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "premium/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "premium/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "premium/login.html")


def logout_view(request):
    logout(request)
    return render(request, "premium/login.html")
