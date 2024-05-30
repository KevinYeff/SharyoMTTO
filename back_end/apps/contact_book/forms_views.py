from .forms import ContactForm, StoreForm, WorkshopForm, MechanicForm
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError


FORMS_DISPONIBLES = ['create_contact',
                     'create_store',
                     'create_workshop',
                     'create_mechanic']

FORMS_CLASSES = {
    'create_contact': ContactForm,
    'create_store': StoreForm,
    'create_workshop': WorkshopForm,
    'create_mechanic': MechanicForm
}

FORM_PLANTILLAS = (('create_contact', 'new_contact.html'),
                   ('create_store', 'new_store.html'),
                   ('create_workshop', 'new_workshop copy.html'),
                   ('create_mechanic', 'new_mechanic.html'))

FROM_MENSAJES = {
    'create_contact': ['Contacto creado exitosamente.',
                       'Error al crear contacto'],
    'create_store': ['Tienda creada exitosamente',
                     'Error al crear tienda'],
    'create_workshop': ['Taller creado exitosamente',
                        'Error al crear taller'],
    'create_mechanic': ['Mecánico creado exitosamente',
                        'Error al crear mecánico']
}

def contactBookforms(request, form_name):
    """
    Método para mostrar al cliente formularios basados en el nombre.
    Args:
        request(Objeto): Objeto del módulo HTTP que contiene información acerca
        de la peticón entrante.

        form_name(Cadena): Parámetro rescatado del url para poder encontrar el
        formulario correspondiente.
    """

    if form_name not in FORMS_DISPONIBLES:
        #message = 'Formulario no disponible'
        #return render(request, '.html', message)
        return HttpResponse('Formulario no disponible')

    if request.method == 'GET':
        try:
            form_class = FORMS_CLASSES[form_name]
            form = form_class()
            context = {
                'form': form
            }
            template = FORM_PLANTILLAS[FORMS_DISPONIBLES.index(form_name)][1]

            return render(request, template, context)
        except Exception as e:
            return HttpResponse('Error: ' + str(e), staus=500)

    elif request.method == 'POST':
        try:
            form_class = FORMS_CLASSES[form_name]
            form = form_class(request.POST)

            if form.is_valid():
                message = FROM_MENSAJES[form_name][0]

                if not form.cleaned_data.get('name') \
                    or not form.cleaned_data.get('email') \
                    or not form.cleaned_data.get('phone'):
                        raise ValidationError('Todos los campos \
                            son obligatorios')
                form.save()

                return HttpResponse(message, status=200)

            else:
                message = FROM_MENSAJES[form_name][0][1]
                return HttpResponse(message, status=400)

        except ValidationError as e:
            return HttpResponse('Error ' + str(e), status=400)
        except Exception as e:
            return HttpResponse('Error ' + str(e), status=500)
