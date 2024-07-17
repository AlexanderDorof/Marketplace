from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from main_app.views import pageNotFoundRedirect
from marketplace.settings import DEBUG, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

urlpatterns = [
    path("", include("main_app.urls")),
    path("registration/", include("register.urls")),
    path("api/", include("rest_api.urls")),
    path("signals/", include("signals.urls")),
    path("admin-panel/", include("custpanel.urls", namespace="admin-panel")),
]

handler404 = pageNotFoundRedirect

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
