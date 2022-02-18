from email.mime import image
from operator import mod
from statistics import mode
from django.db import models

class TourPackage(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    town = models.ManyToManyField('Town', related_name='town')
    image = models.ImageField(blank=True, null=True)
    overview = models.TextField()
    activities = models.TextField()
    departure = models.DateField()
    return_date = models.DateField()
    included = models.TextField()
    cancelation_policy = models.TextField()
    additional_info = models.TextField()
    posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Town(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
