from django.urls import include, path

from .views import FavoriteList, add_to_favorite, contacts, index, info

urlpatterns = [
    path("", index, name="home"),
    path("", include("crud_db.urls")),
    path("info/", info, name="info"),
    path("contacts/", contacts, name="contacts"),
    path("ajax/", add_to_favorite, name="ajax"),
    # authorized users
    path("favorite/", FavoriteList.as_view(), name="favorite"),  # AuthorizedPermission
    path("adminpanel/", index, name="adminpanel"),  # AdminPermission
]
