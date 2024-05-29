from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
from .models import User
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def listUsers(request: HttpRequest):
    """Method that will return a list of users from db

    Args:
        request (HttpRequest): The HTTP request object containing information
        the incoming request.
    """
    if request.method == 'GET':
        try:
            users = list(User.objects.all())
            if not users:
                return HttpResponseNotFound("No users found", status=204)
            # return render(request, 'users.html', {'users': users})
            return JsonResponse(users, safe=False)
        except DatabaseError as e:
            return JsonResponse(
                {
                    'error': 'Database error: ' + str(e)
                },
                status=500)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'No users found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse(
            {
                'error': 'Method not allowed, GET request only'
            },
            status=405)


def register_user(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpRequest(f'Ya esta autenticado como {user.email}.')
    context = {}
   
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            destination =kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form
            
    return render(request,'registration/registro.html' ,context)
    
    
@login_required
def dashboard(request):
    return render(request,'dashboard/dashboard.html', {})
    
def create_user(request):
    """Method that will return a form to create a new user"""
    
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'formulario.html', context)
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Usuario creado exitoxamente")

        
        

        