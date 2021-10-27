from django.db import models
from ..premium.models import Suscribed
# Create your models here.

class Owner_areas(models.Model):
    owner = models.ForeignKey("Suscribed", on_delete=models.CASCADE)
    place_name = models.CharField(max_length=45)
    place_id = models.IntegerField(blank=False)