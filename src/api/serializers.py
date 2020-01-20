from rest_framework import serializers

from api.models import Animal, AnimalType


class AnimalSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'animal_type',
        )


class AnimalTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = AnimalType
        fields = (
            'id',
            'name',
        )
