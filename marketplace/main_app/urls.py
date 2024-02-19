from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

# app_name = 'main'
urlpatterns = [
    path('', index, name='home'),
    path('info', info, name='info'),
    path('contacts', contacts, name='contacts'),
    path('cars/', CarsList.as_view(), name='cars'),
    path('car/<slug:slug>/', CarDetailView.as_view(), name="car_url"),
    path('moto/<slug:slug>/', MotoDetailView.as_view(), name="moto_url"),
    path('service/<int:id>', index, name="service_url"),
    path('motos/', MotosList.as_view(), name='motos'),
    path('services/', ServicesList.as_view(), name='services'),
    path('favorite/', FavoriteList.as_view(), name='favorite'),
    path('publish/', AddPage.as_view(), name='publish'),
    path('car/edit/<slug:slug>/', CarEditView.as_view(), name='edit_car'),
    path('motos/edit/<slug:slug>/', MotoEditView.as_view(), name='edit_moto'),
    path('car/delete/<slug:slug>/', CarDeleteView.as_view(), name='delete_car'),  # Для удаления машины
    path('motocycle/delete/<slug:slug>/', MotoDeleteView.as_view(), name='delete_moto'),  # Для удаления машины
    path('adminpanel/', index, name='adminpanel'),
]
