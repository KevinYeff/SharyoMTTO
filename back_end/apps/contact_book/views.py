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
                return HttpResponse("Contacto creado exitoxamente", status=200)

            else:
                return HttpResponse("Error al crear contacto", status=400)
        except ValidationError as e:
            return HttpResponse("Error: " + str(e), status=400)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    else:
        return HttpResponse("Petición inválida", status=400)


def new_store(request):
    """
    Método que en principio retorna un formulario para crear una
    nueva tienda.

    Args:
        request (objeto): Objeto del módulo HTTP que contiene información acerca
        de la petición entrante.
    """

    if request.method =='GET':
        try:
            form = StoreForm()
            context = {
                'form': form
            }
            return render(request, 'new_store.html', context)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    elif request.method == 'POST':
        try:
            form = StoreForm(request.POST)

            if form.is_valid():

                if not form.cleaned_data.get('name') \
                    or not form.cleaned_data.get('email') \
                    or not form.cleaned_data.get('phone'):
                        raise ValidationError('Todos los campos \
                            son obligatorios')

                form.save()
                return HttpResponse("Tienda creada exitoxamente", status=200)

            else:
                return HttpResponse("Error al crear tienda", status=400)

        except ValidationError as e:
            return HttpResponse("Error: " + str(e), status=400)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    else:
        return HttpResponse("Petición inválida", status=400)


def new_workshop(request):
    """
    Método que en un principio retorna un formulario para crear un taller nuevo
    Args:
        request (objeto): Objeto del módulo HTTP que contiene información acerca
        de la petición entrante.
    """

    if request.method =='GET':
        try:
            form = WorkshopForm
            context = {
                'form': form
            }
            return render(request, 'new_workshop copy.html', context)

        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    elif request.method == 'POST':
        try:
            form = WorkshopForm(request.POST)

            if form.is_valid():

                if not form.cleaned_data.get('name') \
                        or not form.cleaned_data.get('email') \
                        or not form.cleaned_data.get('phone'):
                            raise ValidationError('Todos los campos \
                                son obligatorios')

                form.save()
                return HttpResponse("Taller creado exitosamente",status=200)

            else:
                return HttpResponse('Error al crear el taller', status=400)

        except ValidationError as e:
            return HttpResponse("Error: " + str(e), status=400)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    else:
        return HttpResponse("Petición inválida", status=400)


def new_mechanic(request):
    """
    Método que en principio retorn aun formulario para agregar un nuevo
    mecánico.
    Args:
        request (objeto): Objeto del módulo HTTP que contiene información acerca
        de la petición entrante.
    """
    if request.method =='GET':
        try:
            form = MechanicForm
            context = {
                'form': form
            }
            return render(request, 'new_mechanic.html', context)

        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

    elif request.method == 'POST':
        try:
            form = MechanicForm(request.POST)

            if form.is_valid():

                if not form.cleaned_data.get('name') \
                    or not form.cleaned_data.get('email') \
                    or not form.cleaned_data.get('phone'):
                        raise ValidationError('Todos los campos \
                            son obligatorios')
                form.save()
                return HttpResponse("Mecanico creada exitoxamente", status=200)

            else:
                return HttpResponse('Error al agregar un nuevo mecánico',
                                    status=400)

        except ValidationError as e:
            return HttpResponse("Error: " + str(e), status=400)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)
