from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=50)
    shortname = models.CharField(max_length=3, blank=True)
    phonecode = models.CharField(max_length=7, blank=True)
    
    def __str__(self):
        return self.country
    
    class Meta:
        db_table = 'pais'
        verbose_name = 'Pais'
        verbose_name_plural = 'paises'

class State(models.Model):
    state = models.CharField(max_length=50)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.state
    
    class Meta:
        db_table = 'estados'
        verbose_name = 'Estados'
        verbose_name_plural = 'estados'

class City(models.Model):
    city = models.CharField(max_length=50)
    id_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.city
    
    class Meta:
        db_table = 'ciudad'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'ciudades'
        
        
 # *** SECCION USUARIO ***  
      
 # UserManager para el modelo User    
    
class UserManager(BaseUserManager):
    def create_user(self, username, name, last_name, email, mobile, password, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        user = self.model(email=email, username=username, name=name, last_name=last_name, mobile=mobile, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, name, last_name, email, mobile, password):
        user = self.create_user(
            username, 
            password,  
            name,
            last_name,
            email,
            mobile  
        )
        
        user.is_user = True 
        user.is_superuser = True
        user.is_admin = True
        
        user.save(using=self._db)
        return user   

# Modelo para la tabla de "usuario"
     
class User(AbstractBaseUser):
    
    # Informacion personal
    name = models.CharField('Nombre', max_length=20)
    last_name = models.CharField('Apellido', max_length=20)
    mobile = models.CharField('Celular', max_length=20, blank=False, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField('Correo electronico', unique= True)
    birth_date = models.DateField(default=timezone.now())
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    
    # Informacion de usuario
    username = models.CharField('Nombre de usuario', unique=True, max_length=20)
    
    # Informacion de accesos
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    objects = UserManager()
    date_joined = models.DateTimeField(default=timezone.now())
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'last_name', 'mobile']
    
    def __str__(self):
        return f'Usuario {self.username}'
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
        
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
# *** FIN SECCION USUARIO ***