from django.urls import path
from . import views

urlpatterns = [
    path('new_vehicle/', views.add_vehicle, name='add_vehicle'),
]