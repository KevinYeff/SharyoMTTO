from django.urls import path
from . import views

urlpatterns = [
    path('new_contact/', views.new_contact, name='new_contact'),
    path('new_store/', views.new_store, name='new_store'),
    path('new_workshop/', views.new_workshop, name='new_workshop'),
    path('new_mechanic/', views.new_workshop, name='new_mechanic')
]