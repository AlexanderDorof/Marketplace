from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from marketplace.settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from main_app.views import pageNotFoundRedirect

urlpatterns = [

    path('', include('main_app.urls')),
    path('registration/', include('register.urls')),
    path('api/', include('rest_api.urls')),
    path('signals/', include('signals.urls')),
    path('admin-panel/', include('custpanel.urls', namespace='admin-panel')),

]

handler404 = pageNotFoundRedirect

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
