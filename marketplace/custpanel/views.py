from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.models import User as DjangoUser
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from queryset_sequence import QuerySetSequence

from main_app.models import Car, Motocycle, Service
from main_app.models import User as CustomUser

from .forms import CarForm, MotocycleForm, ServiceForm, UserForm
from .permissions import AdminPermissionsMixin, user_is_admin
from .utils import PaginationMixin


@user_passes_test(test_func=user_is_admin, login_url="register:login")
def admin_home(request):
    context = {"title": "Панель администратора"}
    return render(request, "custpanel/index.html", context=context)


# READ


class VehicleList(AdminPermissionsMixin, PaginationMixin, ListView):
    template_name = "custpanel/list.html"
    paginate_by = 20
    item_name = "custpanel/list/list-cars.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["item_name"] = self.item_name
        context["page"] = (
            int(self.request.GET.get("page", "1")) - 1
        ) * self.paginate_by
        context["items"] = self.paginated_object(
            self.model.objects.all().order_by("id")
        )
        context["page_range"] = self.paginate_page_range(
            total_pages=context["items"].paginator.num_pages,
            page_number=context["items"].number,
        )

        return context


CarsList = type("CarsList", (VehicleList,), {"model": Car, "title": "Каталог машин"})
MotorcyclesList = type(
    "MotorcyclesList",
    (VehicleList,),
    {
        "model": Motocycle,
        "title": "Каталог мотоциклов",
        "item_name": "custpanel/list/list-motorcycles.html",
    },
)
ServicesList = type(
    "ServicesList",
    (VehicleList,),
    {
        "model": Service,
        "title": "Услуги",
        "item_name": "custpanel/list/list-services.html",
    },
)
UserList = type(
    "UserList",
    (VehicleList,),
    {
        "model": CustomUser,
        "title": "Пользователи",
        "item_name": "custpanel/list/list-users.html",
    },
)


# CREATE


class AddItem(AdminPermissionsMixin, CreateView):
    form_class = CarForm
    template_name = "custpanel/create.html"
    extra_context = {"title": "Создать объявление", "vehicle": "автомобиль"}
    login_url = "register:login"
    success_url = reverse_lazy("admin-panel:admin_home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle"] = self.vehicle
        return context

    def get_initial(self):
        initial = super().get_initial()
        pk = self.request.user.pk
        user = CustomUser.objects.get(user_django__pk=pk)
        initial["seller"] = user
        initial["used_car"] = True
        return initial


AddCar = type("AddCar", (AddItem,), {"form_class": CarForm, "vehicle": "автомобиль"})
AddMoto = type(
    "AddMoto", (AddItem,), {"form_class": MotocycleForm, "vehicle": "мотоцикл"}
)
AddService = type(
    "AddService", (AddItem,), {"form_class": ServiceForm, "vehicle": "услуга"}
)


# UPDATE


class ItemEditView(AdminPermissionsMixin, UpdateView):
    extra_context = {"title": "Редактирование записи"}
    template_name = "custpanel/change.html"
    form_class = CarForm
    context_object_name = "item"
    login_url = "register:login"


CarEditView = type(
    "CarEditView",
    (ItemEditView,),
    {"model": Car, "success_url": reverse_lazy("admin-panel:list-cars")},
)
MotoEditView = type(
    "MotoEditView",
    (ItemEditView,),
    {
        "model": Motocycle,
        "form_class": MotocycleForm,
        "success_url": reverse_lazy("admin-panel:list-motorcycles"),
    },
)
ServiceEditView = type(
    "ServiceEditView",
    (ItemEditView,),
    {
        "model": Service,
        "form_class": ServiceForm,
        "success_url": reverse_lazy("admin-panel:list-services"),
    },
)


@user_passes_test(test_func=user_is_admin, login_url="register:login")
def user_edit_view(request, pk):
    user = DjangoUser.objects.get(pk=pk)
    username = user.username
    group = user.groups.values("name")[0]["name"]
    email = user.email
    if request.method == "POST":
        form = UserForm(request.POST)
        # checks whether data are valid:
        if form.is_valid():
            user = DjangoUser.objects.get(pk=pk)
            new_username = form.cleaned_data["username"]
            new_password = form.cleaned_data["password"]
            new_group = form.cleaned_data["group"]
            new_email = form.cleaned_data["email"]
            if new_username != username:
                user.username = new_username
            if new_password:
                user.set_password(new_password)
            if new_group != group:
                new_group_model = Group.objects.get(name=new_group)
                user.groups.set([new_group_model])
            if new_email != email:
                user.email = new_email
            user.save()

            return redirect("admin-panel:list-users", permanent=True)
    form = UserForm(username=username, group=group, email=email)

    return render(
        request,
        "custpanel/change.html",
        {"form": form, "title": "Редактирование записи"},
    )


# DELETE


class VehicleDeleteView(AdminPermissionsMixin, DeleteView):
    model = Car
    extra_context = {"title": "Подтвердить удаление"}
    context_object_name = "item"
    success_url = reverse_lazy("admin-panel:admin_home")
    template_name = "custpanel/confirm_delete.html"


CarDeleteView = type("CarDeleteView", (VehicleDeleteView,), {"model": Car})
MotoDeleteView = type("MotoDeleteView", (VehicleDeleteView,), {"model": Motocycle})
ServiceDeleteView = type("CarDeleteView", (VehicleDeleteView,), {"model": Service})
UserDeleteView = type("UserDeleteView", (VehicleDeleteView,), {"model": DjangoUser})


@user_passes_test(test_func=user_is_admin, login_url="register:login")
def delete_multiselect(request):
    """view allows deletion multiple records in one click"""
    if request.method == "GET":
        # consts
        cars = Car.objects.all()
        motocycles = Motocycle.objects.all()
        services = Service.objects.all()
        users = DjangoUser.objects.all()
        context = {
            "title": "Удалить записи",
            "items": [cars, motocycles, services, users],
        }

    if request.method == "POST":
        # ids of all models intended to delete
        request_dict = dict(request.POST)
        car_ids = request_dict.get("car", None)
        motorcycle_ids = request_dict.get("motocycle", None)
        service_ids = request_dict.get("service", None)
        user_ids = request_dict.get("user", None)

        # querysets of all models intended to delete
        cars = Car.objects.filter(pk__in=car_ids) if car_ids else Car.objects.none()
        motorcycles = (
            Motocycle.objects.filter(pk__in=motorcycle_ids)
            if motorcycle_ids
            else Motocycle.objects.none()
        )
        services = (
            Service.objects.filter(pk__in=service_ids)
            if service_ids
            else Service.objects.none()
        )
        users = (
            DjangoUser.objects.filter(pk__in=user_ids)
            if user_ids
            else DjangoUser.objects.none()
        )

        # combine all querysets in one
        query = QuerySetSequence(cars, motorcycles)
        query = QuerySetSequence(query, services)
        query = QuerySetSequence(query, users)
        query.delete()

        return redirect("admin-panel:delete")

    return render(request, "custpanel/delete.html", context=context)
