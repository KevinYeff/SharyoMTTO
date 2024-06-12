from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Contact_book

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_contact_book(sender, instance, created, **kwargs):
    if created:
        Contact_book.objects.create(user=instance)
