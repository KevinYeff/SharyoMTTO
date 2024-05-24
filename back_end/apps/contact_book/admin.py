from django.contrib import admin
from .models import Contact, Mechanic, Workshop, Specialization, Store, Contact_book

# Register your models here.
admin.site.register(Contact)
admin.site.register(Mechanic)
admin.site.register(Workshop)
admin.site.register(Specialization)
admin.site.register(Store)
admin.site.register(Contact_book)
