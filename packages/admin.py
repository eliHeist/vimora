from django.contrib import admin

from packages.models import TourPackage, Town

# Register your models here.
admin.site.register(TourPackage)
admin.site.register(Town)