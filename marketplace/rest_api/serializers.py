from rest_framework import serializers
from main_app.models import Car, Motocycle


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MotocycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motocycle
        fields = '__all__'
