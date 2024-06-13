from rest_framework import generics, permissions
from .models import Contact_book, Contact, Store, Workshop, Mechanic
from .serializers import ContactSerializer
from .serializers import StoreSerializer, WorkshopSerializer, MechanicSerializer

# ContactBook Views


class ContactBookListView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        contact_book = Contact_book.objects.get(user=user)
        return contact_book


# Contact Views


class AddContactView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        contact_book = self.request.user.contact_book
        serializer.save(contact_book=contact_book)


class ContactDetailview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        contact_id = self.kwargs["id"]
        return Contact.objects.filter(id=contact_id, contact_book=user_cb)


class ContactListview(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        return Contact.objects.filter(contact_book=user_cb)


# Store Views


class AddStoreView(generics.CreateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        contact_book = self.request.user.contact_book
        serializer.save(contact_book=contact_book)


class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        store_id = self.kwargs["id"]
        return Store.objects.filter(id=store_id, contact_book=user_cb)


class StoreListView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        return Store.objects.filter(contact_book=user_cb)


# Workshop Views


class AddWorkshopView(generics.CreateAPIView):
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        contact_book = self.request.user.contact_book
        serializer.save(contact_book=contact_book)


class WorkshopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        workshop_id = self.kwargs["id"]
        return Workshop.objects.filter(id=workshop_id, contact_book=user_cb)


class WorkshopListview(generics.ListCreateAPIView):
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        return Workshop.objects.filter(contact_book=user_cb)


# Mechanic Views


class MechanicListView(generics.ListCreateAPIView):
    serializer_class = MechanicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        return Mechanic.objects.filter(contact_book=user_cb)


class MechanicDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MechanicSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user_cb = self.request.user.contact_book
        mechanic_id = self.kwargs["id"]
        return Mechanic.objects.filter(id=mechanic_id, contact_book=user_cb)


class AddMechanicView(generics.CreateAPIView):
    serializer_class = MechanicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        contact_book = self.request.user.contact_book
        serializer.save(contact_book=contact_book)
