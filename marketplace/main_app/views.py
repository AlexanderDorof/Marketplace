from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from icecream import ic
from django.db.models import Q

from .forms import AddCarForm, AddMotoForm
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *


def index(request):
    context = funcmixin(request, title='Главная страница')
    return render(request, 'main_app/index.html', context=context)


def info(request):
    context = funcmixin(request, title='О магазине')
    return render(request, 'main_app/info.html', context=context)


def contacts(request):
    context = funcmixin(request, title='Контакты')
    return render(request, 'main_app/contacts.html', context=context)


class CarsList(DataMixin, ListView):
    model = Car
    extra_context = {'title': 'Каталог машин', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
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
        c_def = self.get_user_context()
        context = {**context, **c_def}
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
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context

class ServiceDetailView(DataMixin, DetailView):
    model = Service
    template_name = 'main_app/service_description.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание услуги'
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


class MotosList(DataMixin, ListView):
    model = Motocycle
    extra_context = {'title': 'Каталог мотоциклов', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context



class ServicesList(DataMixin, ListView):
    model = Service
    extra_context = {'title': 'Услуги', 'item_name': 'main_app/service.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


class FavoriteList(DataMixin, ListView):
    extra_context = {'title': 'Избранное', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context

    def get_queryset(self):
        djangouser = self.request.user
        user = User.objects.get(user_django=djangouser)
        fav = user.favorite
        cars = list(fav.favorite_cars.all())
        motos = list(fav.favorite_moto.all())
        return cars + motos


class AddCar(DataMixin, CreateView):
    form_class = AddCarForm
    template_name = 'main_app/publish.html'
    extra_context = {'title': 'Создать объявление', 'vehicle': 'автомобиль'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


    def get_initial(self):
        initial = super().get_initial()
        pk = self.request.user.pk
        user = User.objects.get(user_django__pk=pk)
        ic(user)
        initial['seller'] = user
        initial['used_car'] = True
        return initial



class AddMoto(DataMixin, CreateView):
    form_class = AddMotoForm

    template_name = 'main_app/publish.html'
    extra_context = {'title': 'Создать объявление', 'vehicle': 'мотоцикл'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ic([field.name for field in AddMotoForm()._meta.fields])
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context

    def get_initial(self):
        initial = super().get_initial()
        pk = self.request.user.pk
        user = User.objects.get(user_django__pk=pk)
        ic(user)
        initial['seller'] = user
        return initial




class CarEditView(DataMixin, UpdateView):
    model = Car
    extra_context = {'title': 'Редактирование записи'}
    fields = "__all__" # Поля, которые вы хотите редактировать
    template_name = 'main_app/update.html'  # Шаблон для редактирования машины
    success_url = reverse_lazy('cars')  # URL-адрес для перенаправления после успешного редактирования

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


class MotoEditView(DataMixin, UpdateView):
    model = Motocycle
    extra_context = {'title': 'Редактирование записи'}
    fields = "__all__" # Поля, которые вы хотите редактировать
    template_name = 'main_app/update.html'  # Шаблон для редактирования машины
    success_url = reverse_lazy('motos')  # URL-адрес для перенаправления после успешного редактирования

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


class CarDeleteView(DataMixin, DeleteView):
    model = Car
    extra_context = {'title': 'Подтвердить удаление'}
    context_object_name = 'item'
    success_url = reverse_lazy('cars')  # URL, на который перенаправлять после успешного удаления машины
    template_name = 'main_app/confirm_delete.html'  # Шаблон для подтверждения удаления

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


class MotoDeleteView(DataMixin, DeleteView):
    model = Motocycle
    extra_context = {'title': 'Подтвердить удаление'}
    context_object_name = 'item'
    success_url = reverse_lazy('motos')  # URL, на который перенаправлять после успешного удаления машины
    template_name = 'main_app/confirm_delete.html'  # Шаблон для подтверждения удаления

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context