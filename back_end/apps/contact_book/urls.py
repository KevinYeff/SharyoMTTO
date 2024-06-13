from django.urls import path
from .views import (
    ContactBookListView, AddContactView, ContactDetailview, ContactListview,
    AddMechanicView, MechanicDetailView, MechanicListView, AddStoreView,
    StoreDetailView, StoreListView, AddWorkshopView, WorkshopDetailView,
    WorkshopListview
)

urlpatterns = [
    path('', ContactBookListView.as_view(), name='contact_book_list'),
    path('add_contact/', AddContactView.as_view(), name='add-contact'),
    path('contacts/<int:id>', ContactDetailview.as_view(), name='contact-details'),
    path('contacts/', ContactListview.as_view(), name = 'contacts-list'),
    path('add_mechanic/', AddMechanicView.as_view(), name = 'add-mechanic'),
    path('mechanics/<int:id>', MechanicDetailView.as_view(), name = 'mechanic-details'),
    path('mechanics/', MechanicListView.as_view(), name = 'mechanic-list'),
    path('add_store/', AddStoreView.as_view(), name = 'add-store'),
    path('stores/<int:id>', StoreDetailView.as_view(), name = 'store-details'),
    path('stores/', StoreListView.as_view(), name = 'stores-list'),
    path('add_workshop/', AddWorkshopView.as_view(), name = 'add-workshop'),
    path('workshops/<int:id>', WorkshopDetailView.as_view(), name = 'workshop-details'),
    path('workshops/', WorkshopListview.as_view(), name = 'workshops-list'),
]
