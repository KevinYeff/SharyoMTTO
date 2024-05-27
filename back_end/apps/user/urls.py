from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.listUsers),
    path('users/<int:id>/', views.listUsersById)
]
