from django.urls import path
from . import views
from SharyoMTTO.views import home

urlpatterns = [
    path('users/', views.listUsers),
    path('new_user/', views.create_user, name='new_user'),
    path('registro/', views.register_user, name='registro'),
]
