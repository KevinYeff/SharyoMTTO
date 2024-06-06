from django.urls import path
from . import views
from .views import (
    UserVehiclesListView,
    CreateVehicleView,
    VehicleDetailView
)

urlpatterns = [
    path('create_vehicle/', CreateVehicleView.as_view(), name='create_vehicle'),
    path('user_vehicles/', UserVehiclesListView.as_view(), name='user_vehicle'),
    path('user_vehicles/<int:id>/', VehicleDetailView.as_view(), name='vehicle_detail'), 
]