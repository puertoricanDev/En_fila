from django.db import models
from ..premium.models import Suscribed
# Create your models here.

class Owner_areas(models.Model):
    owner = models.ForeignKey("premium.Suscribed", on_delete=models.CASCADE)
    place_name = models.CharField(max_length=45)
    area_id = models.IntegerField(blank=False)
    current_position = models.IntegerField(blank=False, default=0)

class Employee(models.Model):
    fila_admin = models.ForeignKey(
        "premium.Suscribed", on_delete=models.CASCADE)
    fila_employee = models.CharField(max_length=45)
    employee_user = models.CharField(max_length=24)
    employee_passcode = models.PositiveIntegerField(unique=True)
