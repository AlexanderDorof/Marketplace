from django.urls import path
from .views import (
    CarListCreateView, CarDetailView, CarUpdateView, CarDeleteView,
    MotocycleListCreateView, MotocycleDetailView, MotocycleUpdateView, MotocycleDeleteView,
    ServiceListCreateView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView,
    UserListCreateView, UserDetailView
)

app_name = 'restapi'

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<slug:slug>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/update/<slug:slug>/', CarUpdateView.as_view(), name='car-update'),
    path('cars/delete/<slug:slug>/', CarDeleteView.as_view(), name='car-delete'),

    path('motocycles/', MotocycleListCreateView.as_view(), name='moto-list-create'),
    path('motocycles/<slug:slug>/', MotocycleDetailView.as_view(), name='moto-detail'),
    path('motocycles/update/<slug:slug>/', MotocycleUpdateView.as_view(), name='moto-update'),
    path('motocycles/delete/<slug:slug>/', MotocycleDeleteView.as_view(), name='moto-delete'),

    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('services/update/<slug:slug>/', ServiceUpdateView.as_view(), name='service-update'),
    path('services/delete/<slug:slug>/', ServiceDeleteView.as_view(), name='service-delete'),

    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
