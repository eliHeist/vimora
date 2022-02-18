from django.db import models
from packages.models import Town

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Town, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    services = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=30)
    venue = models.CharField(max_length=50)
    image = models.ImageField()
    date = models.DateField()
    information = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name