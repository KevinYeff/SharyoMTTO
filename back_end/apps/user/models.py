from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.utils import timezone

from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=50)
    shortname = models.CharField(max_length=3, blank=True)
    phonecode = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.country

    class Meta:
        db_table = "pais"
        verbose_name = "Pais"
        verbose_name_plural = "paises"


class State(models.Model):
    state = models.CharField(max_length=50)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state

    class Meta:
        db_table = "estados"
        verbose_name = "Estados"
        verbose_name_plural = "estados"


class City(models.Model):
    city = models.CharField(max_length=50)
    id_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.city

    class Meta:
        db_table = "ciudad"
        verbose_name = "Ciudad"
        verbose_name_plural = "ciudades"


# *** SECCION USUARIO ***

# Modelo para la tabla de "usuario"


class User(AbstractBaseUser, PermissionsMixin):

    # Informacion personal
    name = models.CharField("Nombre", max_length=20)
    last_name = models.CharField("Apellido", max_length=20)
    mobile = models.CharField("Celular", max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField("Correo electronico", unique=True)
    birth_date = models.DateField(default=timezone.now())
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    # Informacion de usuario
    username = models.CharField("Nombre de usuario", unique=True, max_length=20)

    # Informacion de accesos
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now())
    last_login = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name", "last_name", "mobile"]

    objects = UserManager()

    def __str__(self):
        return f"Usuario {self.username}"

    @property
    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def tokens(self):
        refresh_token = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh_token),
            "access": str(refresh_token.access_token),
        }

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = "usuario"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.user.name} - passcode"
