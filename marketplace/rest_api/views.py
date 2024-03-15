from rest_framework import generics, permissions

from .serializers import CarSerializer, MotorcycleSerializer, ServiceSerializer, UserSerializer
from main_app.models import Car, Motocycle, Service, User


# CAR
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]


class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


# MOTORCYCLE
class MotorcycleListCreateView(generics.ListCreateAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotorcycleSerializer
    permission_classes = [permissions.AllowAny]


class MotorcycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotorcycleSerializer
    permission_classes = [permissions.AllowAny]


class MotorcycleUpdateView(generics.UpdateAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotorcycleSerializer
    permission_classes = [permissions.IsAuthenticated]


class MotorcycleDeleteView(generics.DestroyAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotorcycleSerializer
    permission_classes = [permissions.IsAuthenticated]


# SERVICES

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


# USER
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
