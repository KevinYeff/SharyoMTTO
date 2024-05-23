from django.db import models
from apps.user.models import City

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=False)
    address = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + " " + self.last_name
    
    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'contacts'       
        
class Specialization(models.Model):
    specialization = models.CharField(max_length=50)
    
    def __str__(self):
        return self.specialization
    
    class Meta:
        db_table = 'specialization'
        verbose_name = 'Specialization'
        verbose_name_plural = 'specializations' 

class Workshop(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True)
    specialization = models.ManyToManyField(Specialization)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'workshop'
        verbose_name = 'Workshop'
        verbose_name_plural = 'workshops'
    
class Mechanic(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=True)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    
    def __str__(self):
        return self.name + " " + self.last_name + " " + self.specialization + " " + self.city
    
    class Meta:
        db_table = 'mechanic'
        verbose_name = 'Mechanic'
        verbose_name_plural = 'mechanics'
        
class Contact_book(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'contact_book'
        verbose_name = 'Contact_book'
        verbose_name_plural = 'Contact_books'