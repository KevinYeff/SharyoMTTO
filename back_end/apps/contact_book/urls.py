from django.urls import path
from . import views

urlpatterns = [
    
    path('new_store/', views.new_store, name='new_store'),
    path('new_workshop/', views.new_workshop, name='new_workshop'),
]