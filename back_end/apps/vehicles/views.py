from django.shortcuts import render
from .forms import VehicleForm
from django.http import HttpResponse

# Create your views here.

def add_vehicle(request):
    """Method that will return a form to add a vehicle"""
    
    if request.method == 'GET':
        form = VehicleForm()
        context = {
            'form': form
        }
        return render(request, 'add_vehicle.html', context)
    
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Vehiculo agregado exitosamente')
