from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.listUsers),
    path('new_user/', views.create_user, name='new_user'),
]
