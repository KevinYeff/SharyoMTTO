from django.db import models
from django.utils import timezone

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
        
class User(models.Model):
    from apps.contact_book.models import Contact_book
    
    # Informacion personal
    name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    mobile = models.CharField(max_length=20, blank=False, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    birth_date = models.DateField(blank=False)

    username = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)
    
    created_date = models.DateField(default=timezone.now())
    update_date = models.DateField(default=timezone.now())
    last_login = models.DateField(default=timezone.now())
    status = models.BooleanField(default=True)
    
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    contact_book = models.ForeignKey(Contact_book, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'