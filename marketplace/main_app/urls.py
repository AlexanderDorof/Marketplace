from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info', info, name='info'),
    path('contacts', contacts, name='contacts'),

    # display all models
    path('cars/', CarsList.as_view(), name='cars'),
    path('motos/', MotosList.as_view(), name='motos'),
    path('services/', ServicesList.as_view(), name='services'),

    # display one item
    path('car/<slug:slug>/', CarDetailView.as_view(), name="car_url"),
    path('moto/<slug:slug>/', MotoDetailView.as_view(), name="moto_url"),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name="service_url"),

    # publish item
    path('publish/car/', AddCar.as_view(), name='publish_car'),  # AuthorizedPermission
    path('publish/moto/', AddMoto.as_view(), name='publish_moto'),  # AuthorizedPermission

    # edit model
    path('car/edit/<slug:slug>/', CarEditView.as_view(), name='edit_car'),  # ModerPermission
    path('motos/edit/<slug:slug>/', MotoEditView.as_view(), name='edit_moto'),  # ModerPermission

    # delete models
    path('car/delete/<slug:slug>/', CarDeleteView.as_view(), name='delete_car'),  # ModerPermission
    path('motocycle/delete/<slug:slug>/', MotoDeleteView.as_view(), name='delete_moto'),  # ModerPermission

    # authorized users
    path('favorite/', FavoriteList.as_view(), name='favorite'),  # AuthorizedPermission
    path('adminpanel/', index, name='adminpanel'),  # AdminPermission todo persmission
]

