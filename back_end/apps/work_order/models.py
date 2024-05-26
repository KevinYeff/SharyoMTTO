from django.db import models
from django.utils import timezone
from apps.vehicles.models import Vehicle
from apps.contact_book.models import Workshop

class Work_order(models.Model):
    
    # mtto CHOICES
    CORRECTIVE = "CORRECTIVO"
    PREVENTIVE = "PREVENTIVO"
    PREDICTIVE = "PREDICTIVO"
    
    FUEL_CHOICES = (
        (CORRECTIVE, "CORRECTIVO"),
        (PREVENTIVE, "PREVENTIVO"),
        (PREDICTIVE, "PREDICTIVO"),)
    
    start_date = models.DateTimeField(default=timezone.now(), blank=False)
    finish_date = models.DateTimeField(blank=True)
    responsable = models.CharField(max_length=50, blank=False)
    fail_detected = models.TextField(max_length=250, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    mtto_type = models.CharField(max_length=15, choices=FUEL_CHOICES, default=CORRECTIVE)
    
    def __str__(self):
        return str(self.id) + " " + self.mtto_type + " " + self.vehicle
    
    class Meta:
        db_table = 'work_order'
        verbose_name = 'Work_order'
        verbose_name_plural = 'work_orders'
    
class Workshops(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    work_order = models.ForeignKey(Work_order, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'workshops'
        verbose_name = 'Workshops'
        verbose_name_plural = 'workshops'