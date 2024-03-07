from django.urls import path

from .views import *


app_name = 'admin-panel'

urlpatterns = [

    path('', admin_home, name='admin_home'),
    path('create/', create, name='create'),
    path('delete/', delete, name='delete'),
    path('change/', change, name='change'),
    path('list/', CarsList.as_view(), name='list'),

]

