from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddCarForm, AddMotoForm
from .models import *
from .utils import *
from .permissions import AuthorPermissionsMixin


def index(request):
    context = funcmixin(request, title='Главная страница')
    return render(request, 'main_app/index.html', context=context)


def info(request):
    context = funcmixin(request, title='О магазине')
    return render(request, 'main_app/info.html', context=context)


def add_to_favorite(request):
    item_pk = request.GET.get('pk')
    item_type = request.GET.get('vehicle')
    pk = request.user.pk
    user = User.objects.get(user_django__pk=pk)
    if item_type == 'car':
        if not user.favorite.favorite_cars.filter(pk=item_pk).exists():
            user.favorite.favorite_cars.add(Car.objects.get(pk=item_pk))
        else:
            car_instance = Car.objects.get(pk=item_pk)
            user.favorite.favorite_cars.remove(car_instance)
    elif item_type == 'motocycle':
        if not user.favorite.favorite_moto.filter(pk=item_pk).exists():
            user.favorite.favorite_moto.add(Motocycle.objects.get(pk=item_pk))
        else:
            moto_instance = Motocycle.objects.get(pk=item_pk)
            user.favorite.favorite_moto.remove(moto_instance)
    return JsonResponse({"image": "/static/static_imgs/heart-icon.svg", "pk": item_pk})


def contacts(request):
    context = funcmixin(request, title='Контакты')
    return render(request, 'main_app/contacts.html', context=context)


class CarsList(DataMixin, PaginationMixin, ListView):
    model = Car
    extra_context = {'title': 'Каталог машин', 'item_name': 'main_app/vehicle.html'}
    template_name = 'main_app/cards.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        context['items'] = self.paginated_object(self.model.objects.all().order_by('id'))
        return context


class CarDetailView(DataMixin, DetailView):
    model = Car
    template_name = 'main_app/item_description.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание товара'
        context['edit_ref'] = 'edit_car'
        context['delete_ref'] = 'delete_car'
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


class MotoDetailView(DataMixin, DetailView):
    model = Motocycle
    template_name = 'main_app/item_description.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание товара'
        context['edit_ref'] = 'edit_moto'
        context['delete_ref'] = 'delete_moto'
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


class ServiceDetailView(DataMixin, DetailView):
    model = Service
    template_name = 'main_app/service_description.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание услуги'
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


class MotosList(DataMixin, PaginationMixin, ListView):
    model = Motocycle
    extra_context = {'title': 'Каталог мотоциклов', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        context['items'] = self.paginated_object(self.model.objects.all().order_by('id'))
        return context


class ServicesList(DataMixin, PaginationMixin, ListView):
    model = Service
    extra_context = {'title': 'Услуги', 'item_name': 'main_app/service.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        context['items'] = self.paginated_object(self.model.objects.all().order_by('id'))
        return context


class FavoriteList(LoginRequiredMixin, DataMixin, PaginationMixin, ListView):
    extra_context = {'title': 'Избранное', 'item_name': 'main_app/vehicle.html'}
    template_name = 'main_app/cards.html'
    login_url = "register:login"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        context['items'] = self.paginated_object(queryset=self.get_queryset())
        return context

    def get_queryset(self):
        djangouser = self.request.user
        user = User.objects.get(user_django=djangouser)
        fav = user.favorite
        cars = list(fav.favorite_cars.all())
        motos = list(fav.favorite_moto.all())
        return cars + motos


class AddCar(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCarForm
    template_name = 'main_app/publish.html'
    extra_context = {'title': 'Создать объявление', 'vehicle': 'автомобиль'}
    login_url = "register:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context

    def get_initial(self):
        initial = super().get_initial()
        pk = self.request.user.pk
        user = User.objects.get(user_django__pk=pk)
        initial['seller'] = user
        initial['used_car'] = True
        return initial


class AddMoto(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMotoForm
    template_name = 'main_app/publish.html'
    extra_context = {'title': 'Создать объявление', 'vehicle': 'мотоцикл'}
    login_url = "register:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context

    def get_initial(self):
        initial = super().get_initial()
        pk = self.request.user.pk
        user = User.objects.get(user_django__pk=pk)
        initial['seller'] = user
        initial['used_car'] = True
        return initial


class CarEditView(AuthorPermissionsMixin, DataMixin, UpdateView):
    model = Car
    extra_context = {'title': 'Редактирование записи'}
    fields = "__all__"
    template_name = 'main_app/update.html'
    success_url = reverse_lazy('cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


class MotoEditView(AuthorPermissionsMixin, DataMixin, UpdateView):
    model = Motocycle
    extra_context = {'title': 'Редактирование записи'}
    fields = "__all__"
    template_name = 'main_app/update.html'
    success_url = reverse_lazy('motos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


class CarDeleteView(AuthorPermissionsMixin, DataMixin, DeleteView):
    model = Car
    extra_context = {'title': 'Подтвердить удаление'}
    context_object_name = 'item'
    success_url = reverse_lazy('cars')  # URL-name, redirected after successful deletion
    template_name = 'main_app/confirm_delete.html'  # Template for confirmation deletion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


class MotoDeleteView(AuthorPermissionsMixin, DataMixin, DeleteView):
    model = Motocycle
    extra_context = {'title': 'Подтвердить удаление'}
    context_object_name = 'item'
    success_url = reverse_lazy('motos')  # URL-name, redirected after successful deletion
    template_name = 'main_app/confirm_delete.html'  # Template for confirmation deletion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context
