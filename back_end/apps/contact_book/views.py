from django.shortcuts import render
from .forms import StoreForm, WorkshopForm, MechanicForm, ContactForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError


# Create your views here.

def new_contact(request):
    """
    Método que en principio retorna un formulario para crear un nuevo contacto.

    Args:
        request(objeto): Objeto del módulo HTTP que contiene información acerca
        de la petición entrante.
    """

    if request.method =='GET':
        try:
            form = ContactForm()
            context = {
                'form': form
            }
            return render(request, 'new_contact.html', context)

        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    elif request.method == 'POST':
        try:
            form = ContactForm(request.POST)

            if form.is_valid():

                if not form.cleaned_data.get('name') \
                    or not form.cleaned_data.get('email') \
                    or not form.cleaned_data.get('phone'):
                        raise ValidationError('Todos los campos \
                            son obligatorios')

                form.save()
                return HttpResponse("Contacto creado exitoxamente")

            else:
                return HttpResponse("Error al crear contacto", status=400)
        except ValidationError as e:
            return HttpResponse("Error: " + str(e), status=400)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    else:
        return HttpResponse("Petición inválida", status=400)


def new_store(request):
    """Method that will return a form to create a new store"""
    if request.method =='GET':
        form = StoreForm()
        context = {
            'form': form
        }
        return render(request, 'new_store.html', context)
    
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tienda creada exitoxamente")
        
def new_workshop(request):
    """Method that will return a form to create a new workshop"""
    if request.method =='GET':
        form = WorkshopForm
        context = {
            'form': form
        }
        return render(request, 'new_workshop.html', context)
    
    if request.method == 'POST':
        form = WorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Taller creada exitoxamente")
        
def new_mechanic(request):
    """Method that will return a form to create a new mechanic"""
    if request.method =='GET':
        form = MechanicForm
        context = {
            'form': form
        }
        return render(request, 'new_workshop.html', context)
    
    if request.method == 'POST':
        form = MechanicForm
        if form.is_valid():
            form.save()
            return HttpResponse("Mecanico creada exitoxamente")