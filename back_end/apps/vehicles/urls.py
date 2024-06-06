from django.urls import path
from . import views
from .views import (
    UserVehiclesListView,
    CreateVehicleView,
    VehicleDetailView,
    MileageRegisterView
)

urlpatterns = [
    path('add_vehicle/', CreateVehicleView.as_view(), name='add_vehicle'),
    path('user_vehicles/', UserVehiclesListView.as_view(), name='user_vehicles'),
    path('user_vehicles/<int:id>/', VehicleDetailView.as_view(), name='vehicle_detail'), 
    
    path('mileage_register/', MileageRegisterView.as_view(), name='mileage_register'),
]