from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Work_order

class WorkOrderSerializer(ModelSerializer):
    # work_orders = SlugRelatedField(slug_field='plate')
    
    class Meta:
        model = Work_order
        fields = ['name',
                  'start_date',
                  'finish_date',
                  'responsable',
                  'fail_detected',
                  'vehicle',
                  'mtto_type']
        
    def create(self, validated_data):
        
        work_order = Work_order.objects.create(
            name = validated_data['name'],
            start_date = validated_data['start_date'],
            finish_date = validated_data['finish_date'],
            responsable = validated_data['responsable'],
            fail_detected = validated_data['fail_detected'],
            vehicle = validated_data['vehicle'],
            mtto_type = validated_data['mtto_type'], 
        )
        work_order.save()
        return work_order
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance