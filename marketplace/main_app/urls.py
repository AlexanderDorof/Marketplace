from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('', CarsList.as_view(), name='cars_list'),
    path('info', info, name='info'),
    path('contacts', contacts, name='contacts'),
    path('cars/', CarsList.as_view(), name='cars'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail_page'),
    path('vehicle/<slug:brand>/<int:id>', index, name="vehicle_url"),
    path('service/<int:id>', index, name="service_url"),
    path('motos/', MotosList.as_view(), name='motos'),
    path('services/', ServicesList.as_view(), name='services'),
    path('favorite/', FavoriteList.as_view(), name='favorite'),
    path('publish/', AddPage.as_view(), name='publish'),
    path('car/<int:pk>/edit/', CarEditView.as_view(), name='edit_car'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='delete_car'),  # Для удаления машины
    path('profile/', index, name='profile'),
    path('login/', index, name='login'),
    path('logout/', index, name='logout'),
    path('adminpanel/', index, name='adminpanel'),
]
