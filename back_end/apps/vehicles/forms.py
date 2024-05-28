from django import forms
from .models import Vehicle

# Fomulario para el registro de un vehiculo
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'plate',
            'model',
            'description',
            'fuel_type',
            'brand',
            'vehicle_category',
            'vehicle_type',
        ]