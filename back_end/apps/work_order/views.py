from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import WorkOrderSerializer
from apps.vehicles.models import Vehicle
from .models import Work_order


# Create your views here.

class MttoCreateView(CreateAPIView):
    """View para crear un nuevo mtto."""
    serializer_class = WorkOrderSerializer
    queryset = Work_order.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        vehicle_id = Vehicle.objects.filter(user_id=user_id)
        if vehicle_id is not None:
            vehicle_instance = get_object_or_404(Vehicle, id=vehicle_id)
            queryset = queryset.filter(vehicle_id=vehicle_instance)
        
        return queryset
    
class MttoListView(ListCreateAPIView):
    """View para listar los mtto de cada vahiculo."""
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        vehicle_id = self.kwargs['vehicle_id']
        return Work_order.objects.filter(vehicle_id=vehicle_id)
    
class MttoDetailView(RetrieveUpdateDestroyAPIView):
    """ View que permite GET/PUT/DELETE de los mttos."""
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        vehicle_id = self.kwargs['vehicle_id']
        return Work_order.objects.filter(vehicle_id=vehicle_id)
    
    
    # serializer_class = WorkOrderSerializer
    
    # # Listing
    
    # def get(self, request, *args, **kwargs):
    #     self.list(request, *args, **kwargs)
    
    # # Creating
    # def post(self, request, *args, **kwargs):
    #     self.create(request, *args, **kwargs)
        
        
        
        
    
    # serializer_class = WorkOrderSerializer
    
    
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     print(self.get_queryset())    
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

