from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import RegistrationForm, AuthenticationForm

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

# *** SECCION REGISTRO ***

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
            destination = get_redirect_if_exists(request)
            if destination: # if destination != None, redirect
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form
            
    return render(request,'registration/registro.html' ,context)

# *** LOGOUT *** 

def logout_user(request):
    logout(request)
    return redirect('home')
    
# *** SECCION LOGIN ***

def login_user(request, *args, **kwargs):
    context = {}
    
    user = request.user
    if user.is_authenticated: 
        return redirect("home")
    
    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))
 
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect('home')
    else:
        form = AuthenticationForm()
        
    context['login_form'] = form
    context['error_message'] = 'Usuario o contraseña incorrectos'
    
    return render(request,'registration/login.html',context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect

# *** VISTA USUARIO ***

def user_view(request, *args, **kwargs):
    
    context = {}
    user_id = kwargs.get('user_id')
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse("El usuario no existe")
    
    if user:
        context['id'] = user.id
        context['username'] = user.username
        context['email'] = user.email
        context['name'] = user.name
        context['last_name'] = user.last_name
        context['mobile'] = user.mobile

    return render(request, 'user/user.html', context)

        
        

        