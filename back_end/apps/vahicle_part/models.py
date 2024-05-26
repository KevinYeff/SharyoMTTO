from django.db import models
from apps.user.models import Country
from apps.work_order.models import Work_order
from apps.contact_book.models import Store
from django.utils import timezone

# Create your models here.

class Part_brand(models.Model):
    brand = models.CharField(max_length=50, blank=False, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    original = models.BooleanField(default=True, blank=False)
    
    def __srt__(self):
        return self.brand
    
    class Meta:
        db_table = 'part_brand'
        verbose_name = 'Part_brand'
        verbose_name_plural = 'part_brands' 
        
class Vehicle_part(models.Model):
    
    # part_type CHOICES
    
    CONSUMABLE = "CONSUMIBLE"
    REPAIRABLE = "REPARABLE"
    NEW = "NUEVO"
    
    FUEL_CHOICES = (
        (CONSUMABLE, "CONSUMIBLE"),
        (REPAIRABLE, "REPARABLE"),
        (NEW, "NUEVO"),)
    
    part = models.CharField(max_length=50, blank=False, unique=True)
    date = models.DateField(defalt=timezone.now(), blank=False)
    part_price = models.FloatField(default=0.00)
    amount = models.FloatField(default=0)
    work_order = models.ForeignKey(Work_order, on_delete=models.CASCADE, on_update=models.CASCADE)
    part_brand = models.ForeignKey(Part_brand, on_delete=models.CASCADE, on_update=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, on_update=models.CASCADE)
    
    def __srt__(self):
        return self.part + " " + self.part_brand
    
    class Meta:
        db_table = 'vehicle_part'
        verbose_name = 'Vehicle_part'
        verbose_name_plural = 'vehicle_parts' 
