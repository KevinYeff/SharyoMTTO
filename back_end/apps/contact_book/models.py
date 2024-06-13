from django.db import models
from apps.user.models import City, State, Country, User

# Create your models here.
class Contact_book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'contact_book'
        verbose_name = 'Contact_book'
        verbose_name_plural = 'Contact_books'

    def __str__(self):
        return f"Contact book of {self.user.username}"


class Specialization(models.Model):
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.specialization

    class Meta:
        db_table = 'specialization'
        verbose_name = 'Specialization'
        verbose_name_plural = 'specializations'


class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=False)
    address = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    contact_book = models.ForeignKey(Contact_book, on_delete=models.CASCADE,
                                     related_name='contacts')

    def __str__(self):
        return self.name + " " + self.last_name

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'contacts'


class Workshop(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True)
    specializations = models.ManyToManyField(Specialization,
                                            related_name='workshop')
    contact_book = models.ForeignKey(Contact_book, on_delete=models.CASCADE,
                                     related_name='workshops')

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
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization,
                                            related_name='mechanics')
    contact_book = models.ForeignKey(Contact_book, on_delete=models.CASCADE,
                                     related_name='mechanics')

    def __str__(self):
        specializations = ', '.join([str(spec) for spec in self.specialization.all()])
        return f"{self.name} {self.last_name} ({specializations}) {self.city}"

    class Meta:
        db_table = 'mechanic'
        verbose_name = 'Mechanic'
        verbose_name_plural = 'mechanics'


class Store(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    mobil = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=50, blank=True)
    specializations = models.ManyToManyField(Specialization,
                                            related_name='stores')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'store'
        verbose_name = 'Store'
        verbose_name_plural = 'stores'
