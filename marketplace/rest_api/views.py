from rest_framework import generics, permissions
from main_app.models import Car, Motocycle, Service, User
from .serializers import CarSerializer, MotocycleSerializer, ServiceSerializer, UserSerializer


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


class MotocycleListCreateView(generics.ListCreateAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    permission_classes = [permissions.AllowAny]


class MotocycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    permission_classes = [permissions.AllowAny]


class MotocycleUpdateView(generics.UpdateAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    permission_classes = [permissions.IsAuthenticated]


class MotocycleDeleteView(generics.DestroyAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    permission_classes = [permissions.IsAuthenticated]


# для Services и User

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


# Дополнительно, для разграничения прав доступа для пользователя с правами администратора:
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
