from django.contrib import admin
from .models import Part_brand, Vehicle_part

# Register your models here.
admin.site.register(Part_brand)
admin.site.register(Vehicle_part)