from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from main_app.models import Car, Motocycle
from .serializers import CarSerializer, MotocycleSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'model', 'year_produced', 'body_type', 'drive_type']


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'slug'


class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'slug'


class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'slug'


class MotocycleListCreateView(generics.ListCreateAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'model', 'year_produced', 'body_type']


class MotocycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    lookup_field = 'slug'


class MotocycleUpdateView(generics.UpdateAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    lookup_field = 'slug'


class MotocycleDeleteView(generics.DestroyAPIView):
    queryset = Motocycle.objects.all()
    serializer_class = MotocycleSerializer
    lookup_field = 'slug'
