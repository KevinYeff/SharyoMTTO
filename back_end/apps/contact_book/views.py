from rest_framework import generics
from .models import Contact_book, Contact, Store, Workshop, Mechanic
from .serializers import ContactBookSerializer, ContactSerializer
from .serializers import StoreSerializer, WorkshopSerializer, MechanicSerializer


# ContactBook Views

class ContactBookListView(generics.ListCreateAPIView):
    serializer_class = ContactBookSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Contact_book.objects.filter(contact__user=user_id)

class ContactBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactBookSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Contact_book.objects.filter(contact__user=user_id)


# Contact Views

class ContactListView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Contact.objects.filter(contact_book__contact__user=user_id)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Contact.objects.filter(contact_book__contact__user=user_id)

# Store Views

class StoreListView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Store.objects.filter(contact_book__contact_user=user_id)

class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Store.objects.filter(contact_book__contact__user=user_id)

# Workshop Views

class WorkshopListView(generics.ListCreateAPIView):
    serializer_class = WorkshopSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Workshop.objects.filter(contact_book__contact__user=user_id)

class WorkshopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkshopSerializer
    lookup_field = 'id'

    def get_query_set(self):
        user_id = self.kwargs['id']
        return Workshop.objects.filter(contact_book__contact__user=user_id)

# Mechanic Views

class MechanicListView(generics.ListCreateAPIView):
    serializer_class = MechanicSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Mechanic.objects.filter(contact_book__contact__user=user_id)

class MechanicDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MechanicSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Mechanic.objects.filter(contact_book__contact__user=user_id)
