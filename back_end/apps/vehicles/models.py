from django.db import models
from django.utils import timezone
from apps.user.models import Country, User


# Create your models here.

class Vehicle_type(models.Model):
    type = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.type
    
    class Meta:
        db_table = 'vehicle_type'
        verbose_name = 'Vehicle_type'
        verbose_name_plural = 'vehicle_types'
    
class Vehicle_category(models.Model):
    category = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=250, blank=False)
    
    def __str__(self):
        return self.category
    
    class Meta:
        db_table = 'vehicle_category'
        verbose_name = 'Vehicle_category'
        verbose_name_plural = 'vehicle_categories'
    
class Vehicle_brand(models.Model):
    brand = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    vehicle_types = models.ManyToManyField(Vehicle_type)
    vehicle_categories = models.ManyToManyField(Vehicle_category)
    
    def __str__(self):
        return self.brand 
    
    class Meta:
        db_table = 'vehicle_brand'
        verbose_name = 'Vehicle_brand'
        verbose_name_plural = 'vehicle_brands'
    
class Vehicle(models.Model):
    
    # fuel_type CHOICES
    ELETRIC = "ELECTRICO"
    EXTRA = "EXTRA"
    DIESEL = "DIESEL"
    GASOLINE = "GASOLINA"
    GAS = "GAS"
    HYBRID = "HIBRIDO"
    
    FUEL_CHOICES = (
        (ELETRIC, "ELECTRICO"),
        (EXTRA, "EXTRA"),
        (DIESEL, "DIESEL"),
        (GASOLINE, "GASOLINA"),
        (GAS, "GAS"),)
    
    plate = models.CharField(max_length=10, unique=True)
    model = models.IntegerField(max_length=4, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    fuel_type = models.CharField(max_length=15, choices=FUEL_CHOICES, default=GASOLINE)
    
    user = models.ForeignKey(User, related_name= "user", on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Vehicle_brand, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle_category = models.ForeignKey(Vehicle_category, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'vehicle'
        verbose_name = 'Vehicle'
        verbose_name_plural = 'vehicles'
    
class Consumption(models.Model):
    km_traveled = models.FloatField(blank=False, null=False)
    liters_amount = models.FloatField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    date = models.DateField(default=timezone.now())
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.date)
    
    class Meta:
        db_table = 'consumption'
        verbose_name = 'Consumption'
        verbose_name_plural = 'consumptions'
        
class Mileage(models.Model):
    mileage = models.IntegerField(blank=False)
    last_date = models.DateField(default=timezone.now)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.date)
    
    class Meta:
        db_table = 'mileage'
        verbose_name = 'Mileage'
        verbose_name_plural = 'mileage'