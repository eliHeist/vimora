from multiprocessing import Event
from django.contrib import admin

from main.models import Hotel, Event

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Event)
