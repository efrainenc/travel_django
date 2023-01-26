from django.contrib import admin
from .models import Location, Spot # import the Location and Spot model from models.py


# Register your models here. This will add the models to the admin panel.
admin.site.register(Location)
admin.site.register(Spot)
