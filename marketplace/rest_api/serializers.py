from rest_framework import serializers
from main_app.models import Car, Motocycle, Service, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_seller(self, obj):
        return {"name": obj.seller.name, "id": obj.seller.id}


class MotocycleSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Motocycle
        fields = '__all__'

    def get_seller(self, obj):
        return {"name": obj.seller.name, "id": obj.seller.id}


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
