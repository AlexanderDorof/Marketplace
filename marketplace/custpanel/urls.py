from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'admin-panel'

urlpatterns = [

    path('', models, name='models'),
    path('create/', create, name='create'),
    path('delete/', delete, name='delete'),
    path('change/', change, name='change'),
    path('list/', list, name='list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
