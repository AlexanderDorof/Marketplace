from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from marketplace.settings import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)