from django.contrib import admin
from .models import Contact, Mechanic, Workshop

# Register your models here.
admin.site.register(Contact)
admin.site.register(Mechanic)
admin.site.register(Workshop)