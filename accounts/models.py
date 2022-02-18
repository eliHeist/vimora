import imp
from django.db import models
from django.contrib.auth.models import AbstractUser
from packages.models import TourPackage
from main.models import Event

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    booked_tours = models.ManyToManyField(TourPackage, related_name='users')
    booked_events = models.ManyToManyField(Event, related_name='users')
