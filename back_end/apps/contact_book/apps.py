from django.apps import AppConfig


class ContactBookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contact_book'

    def ready(self):
        import apps.contact_book.signals
