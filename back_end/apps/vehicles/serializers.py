from rest_framework.serializers import ModelSerializer
from .models import Vehicle
from apps.user.models import User


class VehicleSerializer(ModelSerializer): 
  
    class Meta:
        model = Vehicle
        fields = '__all__'
        
    def create(self, validated_data):
        return Vehicle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

class UserVehiclesListSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ['id']