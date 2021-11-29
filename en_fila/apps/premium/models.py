from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta
# Create your models here.


class User(AbstractUser):
    pass

def get_deadline():
    return datetime.today() + timedelta(days=30)

class Suscribed(models.Model):
    suscriber = models.ForeignKey("User", on_delete=models.CASCADE, related_name="suscriber")
    business_name = models.CharField(max_length=45)
    business_phone = PhoneNumberField(blank=True,unique = False)
    first_suscription = models.DateTimeField(default=timezone.now)
    #valid_to = models.DateTimeField(get_deadline())
    expired = models.BooleanField(default=False)
    areas_suscribed = models.PositiveIntegerField(default=4)
