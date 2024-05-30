from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User

# Formulariop para el registro de nuevos usuarios
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=20, help_text='Requerido. agrega un email valido')
    
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'name',
            'last_name',
            'mobile',
            'password1',
            'password2',
        )
        
        # Metodo que verifica si el email se encuentra registrado
        def clean_email(self):
            email = self.cleaned_data['email'].lower()
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except Exception as e:
                return email
            raise forms.ValidationError(f'El email: {email}, ya esta en uso')
        
        # Metodo que verifica si el username ya esta en uso
        def clean_username(self):
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except Exception as e:
                return username
            raise forms.ValidationError(f'El numbre de usuario: {username}, ya esta en uso')
        

class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'password',)
        
        
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Email y/o contraseña incorrectos')