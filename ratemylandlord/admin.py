from django.contrib import admin
from .models import Landlord, Property, Rating

# Register your models here.
admin.site.register(Landlord)
admin.site.register(Property)
admin.site.register(Rating)
