from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from .models import Vehicle
from apps.user.models import User
from .serializers import UserVehiclesListSerializer, VehicleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
    
class UserVehiclesListView(GenericAPIView):
    """ View que muestra la lista de vehiculos del usuario."""
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = self.request.user
        vehicles = Vehicle.objects.filter(user=user)
        serializer = self.serializer_class(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    
class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    """ View que muestra la información de cada vehiculo."""
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        vehicle_id = self.kwargs['id']
        # print(user_id)
        return Vehicle.objects.filter(id=vehicle_id)
    
    # def get(self, vehicle_id, request):
    #     user = request.user
    #     vehicle = Vehicle.objects.filter(id=vehicle_id)
    #     serializer = self.serializer_class(vehicle)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
        
    

    

class CreateVehicleView(CreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    

  

            

