from django.urls import path
from .views import CarListCreateView, CarDetailView, CarUpdateView, CarDeleteView, MotocycleListCreateView, \
    MotocycleDetailView, MotocycleUpdateView, MotocycleDeleteView

app_name = 'restapi'

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('car/<slug:slug>/', CarDetailView.as_view(), name='car-detail'),
    path('car/update/<slug>/', CarUpdateView.as_view(), name='car-update'),
    path('car/delete/<slug>/', CarDeleteView.as_view(), name='car-delete'),

    path('motos/', MotocycleListCreateView.as_view(), name='moto-list-create'),
    path('moto/<slug>/', MotocycleDetailView.as_view(), name='moto-detail'),
    path('moto/update/<slug>/', MotocycleUpdateView.as_view(), name='moto-update'),
    path('moto/delete/<slug>/', MotocycleDeleteView.as_view(), name='moto-delete'),
]


