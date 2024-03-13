from django.urls import path

from .views import *


app_name = 'admin-panel'

urlpatterns = [

    path('', admin_home, name='admin_home'),

    # display list
    path('list/cars/', CarsList.as_view(), name='list-cars'),
    path('list/motorcycles/', MotorcyclesList.as_view(), name='list-motorcycles'),
    path('list/services/', ServicesList.as_view(), name='list-services'),
    path('list/users/', UserList.as_view(), name='list-users'),

    # publish item
    path('create/car/', AddCar.as_view(), name='create-car'),
    path('create/motorcycle/', AddMoto.as_view(), name='create-motorcycle'),
    path('create/service/', AddService.as_view(), name='create-service'),


    path('delete/', delete, name='delete'),

    # delete models
    path('car/delete/<slug:slug>/', CarDeleteView.as_view(), name='delete_car'),  # ModerPermission
    path('motorcycle/delete/<slug:slug>/', MotoDeleteView.as_view(), name='delete_motorcycle'),  # ModerPermission
    path('service/delete/<slug:slug>/', ServiceDeleteView.as_view(), name='delete_service'),  # ModerPermission
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),  # ModerPermission

    # edit model
    path('car/edit/<slug:slug>/', CarEditView.as_view(), name='edit_car'),  # ModerPermission
    path('motors/edit/<slug:slug>/', MotoEditView.as_view(), name='edit_motorcycle'),  # ModerPermission
    path('service/edit/<slug:slug>/', ServiceEditView.as_view(), name='edit_service'),  # ModerPermission

]

