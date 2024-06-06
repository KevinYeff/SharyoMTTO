from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Vehicle, Mileage, Consumption
from apps.user.models import User


class VehicleSerializer(ModelSerializer): 

    class Meta:
        model = Vehicle
        fields = ['plate', 
                  'model', 
                  'description', 
                  'fuel_type', 
                  'brand', 
                  'vehicle_category', 
                  'vehicle_type',
                  'user']
        
    def create(self, validated_data):
        vehicle = Vehicle.objects.create(
            plate = validated_data['plate'],
            model = validated_data['model'],
            description = validated_data['description'],
            fuel_type = validated_data['fuel_type'],
            brand = validated_data['brand'],
            vehicle_category = validated_data['vehicle_category'], 
            user = validated_data.get('user')
        )
        
        return vehicle
    

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance





class MiliageSerializer(ModelSerializer):
    vehicle = VehicleSerializer(many=True)
    
    class Meta:
        model = Mileage
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


class ComsuptionSerializer(ModelSerializer):
    class Meta:
        model = Mileage
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
        