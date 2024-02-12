from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info', info, name='info'),
    path('contacts', contacts, name='contacts'),
    path('cars/', CarsList.as_view(), name='cars'),
    path('vehicle/<slug:brand>/<int:id>', index, name="vehicle_url"),
    path('service/<int:id>', index, name="service_url"),
    path('motos/', MotosList.as_view(), name='motos'),
    path('services/', ServicesList.as_view(), name='services'),
    path('favorite/', FavoriteList.as_view(), name='favorite'),
    path('publish/', AddPage.as_view(), name='publish'),
    path('profile/', index, name='profile'),
    path('login/', index, name='login'),
    path('logout/', index, name='logout'),
    path('adminpanel/', index, name='adminpanel'),
]
