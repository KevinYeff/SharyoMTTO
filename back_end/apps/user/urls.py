from django.urls import path
from . import views
from SharyoMTTO.views import home

urlpatterns = [
    path('users/', views.listUsers),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registro/', views.register_user, name='registro'),
]
