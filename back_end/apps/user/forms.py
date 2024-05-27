from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'last_name',
            'mobile',
            'phone',
            'email',
            'birth_date',
            'username',
            'password',
            'city',      
        ]