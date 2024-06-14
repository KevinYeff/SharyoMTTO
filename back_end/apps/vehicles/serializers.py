from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ImageField, SlugRelatedField
from .models import Vehicle, Mileage, Consumption
from apps.user.models import User
from apps.work_order.serializers import WorkOrderSerializer


class VehicleSerializer(ModelSerializer): 
    image = ImageField(max_length=None, use_url=True)
    brand = SlugRelatedField(many= True, read_only=True, slug_field='brand')
    vehicle_category = SlugRelatedField(many= True, read_only=True, slug_field='category')
    vehicle_type = SlugRelatedField(many= True, read_only=True, slug_field='type')
    # work_orders = WorkOrderSerializer(many=True)
    
    class Meta:
        model = Vehicle
        fields = ['plate', 
                  'model', 
                  'description', 
                  'fuel_type', 
                  'brand', 
                  'vehicle_category', 
                  'vehicle_type',
                  'image',
                  'user']
        
    def create(self, validated_data):
        vehicle = Vehicle.objects.create(
            plate = validated_data['plate'],
            model = validated_data['model'],
            description = validated_data['description'],
            fuel_type = validated_data['fuel_type'],
            brand = validated_data.get('brand'),
            vehicle_type = validated_data.get('vehicle_type'),
            vehicle_category = validated_data.get('vehicle_category'), 
            user = validated_data.get('user'),
            image = validated_data.get('image')
        )
        vehicle.save()
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
    
    class Meta:
        model = Mileage
        fields = ['mileage', 'date', 'vehicle']
                
    def create(self, validated_data):
        mileage = Mileage.objects.create(
            mileage = validated_data['mileage'],
            date = validated_data['date'],
            vehicle = validated_data['vehicle'],
        )  
        return mileage
           
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
        model = Consumption
        fields = ['km_traveled', 'amount', 'price', 'date', 'vehicle']
        
    def create(self, validated_data):
        consumption = Consumption.objects.create(
            km_traveled = validated_data['km_traveled'],
            amount = validated_data['amount'],
            price = validated_data['price'],
            date = validated_data['date'],
            vehicle = validated_data['vehicle'],
        )  
        return consumption
        
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
        
    def delete(self, instance):
        instance.delete()
        return instance    
        