from django.urls import path
from .views import (
    ContactBookListView, ContactBookDetailView,
    ContactListView, ContactDetailView,
    StoreListView, StoreDetailView,
    WorkshopListView, WorkshopDetailView,
    MechanicListView, MechanicDetailView
)

urlpatterns = [
    path('user/<int:id>/contact_book/', ContactBookListView.as_view(), name='contact_book_list'),
    path('user/<int:id>/contact_book/<int:id>/', ContactBookDetailView.as_view(), name='contact_book_detail'),
    path('user/<int:id>/contact_book/contacts/', ContactListView.as_view(), name='contact_list'),
    path('user/<int:id>/contact_book/contacts/<int:id>/', ContactDetailView.as_view(), name='contact_detail'),
    path('user/<int:id>/contact_book/stores/', StoreListView.as_view(), name='store_list'),
    path('user/<int:id>/contact_book/stores/<int:id>/', StoreDetailView.as_view(), name='store_detail'),
    path('user/<int:id>/contact_book/workshops/', WorkshopListView.as_view(), name='workshop_list'),
    path('user/<int:id>/contact_book/workshops/<int:id>/', WorkshopDetailView.as_view(), name='workshop_detail'),
    path('user/<int:id>/contact_book/mechanics/', MechanicListView.as_view(), name='mechanic_list'),
    path('user/<int:id>/contact_book/mechanics/<int:id>/', MechanicDetailView.as_view(), name='mechanic_detail'),
]
