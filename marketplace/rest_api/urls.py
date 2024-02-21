# urls.py
from django.urls import path
from .views import CarListCreateView, CarDetailView, CarUpdateView, CarDeleteView, MotocycleListCreateView, \
    MotocycleDetailView, MotocycleUpdateView, MotocycleDeleteView

urlpatterns = [
    path('models/cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('model/car/<slug>/', CarDetailView.as_view(), name='car-detail'),
    path('model/car/<slug>/update/', CarUpdateView.as_view(), name='car-update'),
    path('model/car/<slug>/delete/', CarDeleteView.as_view(), name='car-delete'),

    path('models/motos/', MotocycleListCreateView.as_view(), name='moto-list-create'),
    path('model/moto/<slug>/', MotocycleDetailView.as_view(), name='moto-detail'),
    path('model/moto/<slug>/update/', MotocycleUpdateView.as_view(), name='moto-update'),
    path('model/moto/<slug>/delete/', MotocycleDeleteView.as_view(), name='moto-delete'),
]


