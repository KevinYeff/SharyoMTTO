from rest_framework import serializers
from .models import Contact_book, Contact, Store, Workshop, Mechanic, Specialization


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'



class StoreSerializer(serializers.ModelSerializer):

    specializations = SpecializationSerializer(many = True)

    class Meta:
        model = Store
        fields = '__all__'

    def create(self, validated_data):
        specializations_data = validated_data.pop('specializations')
        store = Store.objects.create(**validated_data)
        for specialization_data in specializations_data:
            specialization, created = Specialization.objects.create(store=store, **specialization_data)
            store.specializations.add(specialization)
        return store

    def update(self, instance, validated_data):
        specializations_data = validated_data.pop('specializations')
        instance = super().update(instance, validated_data)
        instance.specializations.clear()

        for specialization_data in specializations_data:
            specialization, created = Specialization.objects.get_or_create(store=instance, **specialization_data)
            instance.specializations.add(specialization)
        return instance


class WorkshopSerializer(serializers.ModelSerializer):

    specializations = SpecializationSerializer(many = True)

    class Meta:
        model = Workshop
        fields = '__all__'

    def create(self, validated_data):
        specializations_data = validated_data.pop('specializations')
        workshop = Workshop.objects.create(**validated_data)

        for specialization_data in specializations_data:
            specialization, created = Specialization.objects.get_or_create(**specialization_data)
            workshop.specializations.add(specialization)

        return workshop

    def update(self, instance, validated_data):
        specializations_data = validated_data.pop('specializations')
        instance = super().update(instance, validated_data)
        instance.specializations.clear()

        for specialization_data in specializations_data:
            specialization, created = Specialization.objects.get_or_create(**specialization_data)
            instance.specializations.add(specialization)
        return instance


class MechanicSerializer(serializers.ModelSerializer):

    specializations = SpecializationSerializer(many=True)

    class Meta:
        model = Mechanic
        fields = '__all__'

    def create(self, validated_data):
        specializations_data = validated_data.pop('specializations')
        mechanic = Mechanic.objects.create(**validated_data)

        for specialization_data in specializations_data:
            specialization, created = Specialization.objects.get_or_create(**specialization_data)
            mechanic.specializations.add(specialization)
        return mechanic

    def update(self, instance, validated_data):
        specializations_data = validated_data.pop('specializations')
        instance = super().update(instance, validated_data)
        instance.specializations.clear()

        for specialization_data in specializations_data:
            specialization, created = Specialization.objects.get_or_create(**specialization_data)
            instance.specializations.add(specialization)
        return instance


class ContactBookSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    workshops = WorkshopSerializer(many=True, read_only=True)
    mechanics = MechanicSerializer(many=True, read_only=True)
    stores = StoreSerializer(many=True, read_only=True)

    class Meta:
        model = Contact_book
        fields = ('id', 'user', 'contacts', 'workshops', 'mechanics', 'stores')
