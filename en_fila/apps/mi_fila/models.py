from datetime import date
from django.db import models
from django.db.models import CharField, Model
from ..premium.models import Suscribed
from ..management.models import Owner_areas
from django.utils import timezone


# Create your models here.
class mi_fila(models.Model):
    owner = models.ForeignKey("premium.Suscribed", on_delete=models.CASCADE, related_name="owner")
    owner_places = models.CharField(max_length=45)
    persona = models.CharField(max_length=50)
    llegada = models.DateTimeField(default=timezone.now)
    posicion = models.PositiveIntegerField(blank=False)
    area_id = models.PositiveIntegerField(blank=False)

    def serialize(self):
        return {
            "fila_id": self.id,
            "lugar" : self.owner_places,
            "posicion": self.posicion,
            "persona": self.persona,
            "area_id": self.area_id,
            
        }
    
