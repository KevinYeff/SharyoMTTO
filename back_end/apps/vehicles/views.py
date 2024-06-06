from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from .models import Vehicle
from .serializers import VehicleSerializer, MiliageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Vehicle Views   
class UserVehiclesListView(GenericAPIView):
    """ View que devuelve el listado de vehiculos del usuario."""
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = self.request.user
        vehicles = Vehicle.objects.filter(user=user)
        serializer = self.serializer_class(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    """ View que permite GET/PUT/DELETE de los vehiculos."""
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        vehicle_id = self.kwargs['id']
        return Vehicle.objects.filter(id=vehicle_id)
        
class CreateVehicleView(CreateAPIView):
    """View para la creación de un vehiculo"""
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  

# Mileage view

class MileageRegisterView(CreateAPIView):
    """View para agregar un registro de kilometraje"""
    serializer_class = MiliageSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        

