from django.contrib import admin
from .models import mi_fila
from apps.premium.models import Suscribed
# Register your models here.

admin.site.register(mi_fila)
admin.site.register(Suscribed)
