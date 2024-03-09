from django.urls import path

from .views import *


app_name = 'admin-panel'

urlpatterns = [

    path('', admin_home, name='admin_home'),

    # display list
    path('list/cars/', CarsList.as_view(), name='list-cars'),
    path('list/motorcycles/', MotorcyclesList.as_view(), name='list-motorcycles'),
    path('list/services/', ServicesList.as_view(), name='list-services'),

    # publish item
    path('create/car/', AddCar.as_view(), name='create-car'),
    path('create/motorcycle/', AddMoto.as_view(), name='create-motorcycle'),
    path('create/service/', AddService.as_view(), name='create-service'),


    path('delete/', delete, name='delete'),
    path('change/', change, name='change'),


]

