from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Vehicle_brand)
admin.site.register(Vehicle_category)
admin.site.register(Vehicle_type)
admin.site.register(Vehicle)
admin.site.register(Mileage)
admin.site.register(Consumption)