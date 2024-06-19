from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(_("Intruduzca un correo electronico valido"))
        
    def create_user(self, username, name, last_name, email, mobile, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Se requiere un correo electronico."))
        
        if not name:
            raise ValueError(_("Se requiere un nombre."))
        
        if not last_name:
            raise ValueError(_("Se requiere un apellido."))
        
        if not mobile:
            raise ValueError(_("Se requiere un numero de telefono mobil."))
        
        
        user = self.model(email=email, username=username, name=name, last_name=last_name, mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, name, last_name, email, mobile, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_admin', True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('is_staff must be true for admin user'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is_superuser must be true for admin user'))
            
        user = self.create_user(
            username, name, last_name, email, mobile, password, **extra_fields 
        )
        user.save(using=self._db)
        
        return user