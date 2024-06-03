from rest_framework import serializers
from .models import Contact_book, Contact, Store, Workshop, Mechanic


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

    def create(self, validated_data):
        return Store.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'

    def create(self, validated_data):
        return Workshop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance



class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'

    def create(self, validated_data):
        return Mechanic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance



class ContactBookSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    stores = StoreSerializer(many=True)
    workshops = WorkshopSerializer(many=True)
    mechanics = MechanicSerializer(many=True)

    class Meta:
        model = Contact_book
        fields = '__all__'

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        stores_data = validated_data.pop('stores')
        workshops_data = validated_data.pop('workshops')
        mechanics_data = validated_data.pop('mechanics')

        contact_book = Contact_book.objects.create(**validated_data)

        for contact_data in contacts_data:
            Contact.objects.create(contact_book=contact_book, **contact_data)

        for store_data in stores_data:
            Store.objects.create(contact_book=contact_book, **store_data)

        for workshop_data in workshops_data:
            Workshop.objects.create(contact_book=contact_book, **workshop_data)

        for mechanic_data in mechanics_data:
            Mechanic.objects.create(contact_book=contact_book, **mechanic_data)

        return contact_book

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts')
        stores_data = validated_data.pop('stores')
        workshops_data = validated_data.pop('workshops')
        mechanics_data = validated_data.pop('mechanics')


        instance.contacts.all().delete()
        instance.stores.all().delete()
        instance.workshops.all().delete()
        instance.mechanics.all().delete()

        for contact_data in contacts_data:
            Contact.objects.create(contact_book=instance, **contact_data)

        for store_data in stores_data:
            Store.objects.create(contact_book=instance, **store_data)

        for workshop_data in workshops_data:
            Workshop.objects.create(contact_book=instance, **workshop_data)

        for mechanic_data in mechanics_data:
            Mechanic.objects.create(contact_book=instance, **mechanic_data)

        instance.save()
        return instance

    def delete(self, instance):
        instance.contacts.all().delete()
        instance.stores.all().delete()
        instance.workshops.all().delete()
        instance.mechanics.all().delete()
        instance.delete()
        return instance
