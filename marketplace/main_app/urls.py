from django.urls import path, include

from .views import *
from main_app.management.insert_db import insertcars, insertmotos

urlpatterns = [
    path('', index, name='home'),
    path('', include('crud_db.urls')),
    path('info/', info, name='info'),
    path('contacts/', contacts, name='contacts'),
    path('ajax/', add_to_favorite, name='ajax'),


    # authorized users
    path('favorite/', FavoriteList.as_view(), name='favorite'),  # AuthorizedPermission
    path('adminpanel/', index, name='adminpanel'),  # AdminPermission

]
