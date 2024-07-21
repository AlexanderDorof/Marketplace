from django.urls import path

from .views import (
    AddCar,
    AddMoto,
    AddService,
    CarDeleteView,
    CarEditView,
    CarsList,
    MotoDeleteView,
    MotoEditView,
    MotorcyclesList,
    ServiceDeleteView,
    ServiceEditView,
    ServicesList,
    UserDeleteView,
    UserList,
    admin_home,
    delete_multiselect,
    user_edit_view,
)

app_name = "admin-panel"

urlpatterns = [
    path("", admin_home, name="admin_home"),
    # display all models
    path("list/cars/", CarsList.as_view(), name="list-cars"),
    path("list/motorcycles/", MotorcyclesList.as_view(), name="list-motorcycles"),
    path("list/services/", ServicesList.as_view(), name="list-services"),
    path("list/users/", UserList.as_view(), name="list-users"),
    # publish item
    path("create/car/", AddCar.as_view(), name="create-car"),
    path("create/motorcycle/", AddMoto.as_view(), name="create-motorcycle"),
    path("create/service/", AddService.as_view(), name="create-service"),
    # edit model
    path("car/edit/<slug:slug>/", CarEditView.as_view(), name="edit_car"),
    path("motors/edit/<slug:slug>/", MotoEditView.as_view(), name="edit_motorcycle"),
    path("service/edit/<slug:slug>/", ServiceEditView.as_view(), name="edit_service"),
    path("user/edit/<int:pk>/", user_edit_view, name="edit_user"),
    # delete models
    path("car/delete/<slug:slug>/", CarDeleteView.as_view(), name="delete_car"),
    path(
        "motorcycle/delete/<slug:slug>/",
        MotoDeleteView.as_view(),
        name="delete_motorcycle",
    ),
    path(
        "service/delete/<slug:slug>/",
        ServiceDeleteView.as_view(),
        name="delete_service",
    ),
    path("user/delete/<int:pk>/", UserDeleteView.as_view(), name="delete_user"),
    # delete multiple records
    path("delete/", delete_multiselect, name="delete"),
]
