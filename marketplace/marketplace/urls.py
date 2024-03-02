from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from marketplace.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('registration/', include('register.urls')),
    path('api/', include('rest_api.urls')),
    path('signals/', include('signals.urls')),
    path('models/', include('custpanel.urls')),

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
