from django import forms
from .models import Workshop, Store, Mechanic, Contact

# Formulario para agregar contactos a la agenda
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'last_name',
            'phone',
            'mobil',
            'email',
            'address',
            'country',
            'state',
            'city',
        ]        
        
# Formulario para agregar una nueva tienda
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'phone',
            'mobil',
            'email',
            'country',
            'state',
            'city',
            'address',
        ]


# Formulario para agregar una nuevo taller
class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = [
            'name',
            'phone',
            'mobil',
            'email',
            'country',
            'state',
            'city',
            'address',
            'specialization',
        ]
        
# Formulario para agregar un nuevo mecanico
class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = [
            'name',
            'last_name',
            'phone',
            'mobil',
            'email',
            'workshop',
            'country',
            'state',
            'city',
            'specialization',
        ]