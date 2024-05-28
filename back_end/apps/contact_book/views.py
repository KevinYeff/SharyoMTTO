from django.shortcuts import render
from .forms import StoreForm, WorkshopForm, MechanicForm, ContactForm
from django.http import HttpResponse

# Create your views here.

def new_contact(request):
    """Method that will return a form to create a new contact"""
    if request.method =='GET':
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'new_contact.html', context)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contacto creado exitoxamente")
    
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