from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', book_list, name='book_list'),
    path('car_models/', car_models, name='car_models'),
    path('car_create/', car_create, name='car_create'),
    path('car_delete/', car_delete, name='car_delete'),
    path('car_change/', car_change, name='car_change'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)