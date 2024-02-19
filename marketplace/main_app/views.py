from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AddCarForm
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'main_app/index.html', {'title': 'Главная страница'})


def info(request):
    return render(request, 'main_app/info.html', {'title': 'О магазине'})


def contacts(request):
    return render(request, 'main_app/contacts.html', {'title': 'Контакты'})


class CarsList(ListView):
    model = Car
    extra_context = {'title': 'Каталог машин', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'main_app/full_car_description.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_moderator'] = self.request.user.groups.filter(name='moderator').exists() or self.request.user.groups.filter(name='admin').exists()
        context['is_moderator'] = True
        return context

class MotoDetailView(DetailView):
    model = Motocycle
    template_name = 'main_app/full_moto_description.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_moderator'] = self.request.user.groups.filter(name='moderator').exists() or self.request.user.groups.filter(name='admin').exists()
        context['is_moderator'] = True
        return context



class MotosList(ListView):
    model = Motocycle
    extra_context = {'title': 'Каталог мотоциклов', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'


class ServicesList(ListView):
    model = Service
    extra_context = {'title': 'Услуги', 'item_name': 'main_app/service.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'


class FavoriteList(ListView):
    extra_context = {'title': 'Услуги', 'item_name': 'main_app/vehicle.html'}
    context_object_name = 'items'
    template_name = 'main_app/cards.html'

    def get_queryset(self):
        user = User.objects.get(pk=2)
        fav = user.favorite
        cars = list(fav.favorite_cars.all())
        motos = list(fav.favorite_moto.all())
        return cars + motos


class AddPage(CreateView):
    form_class = AddCarForm
    template_name = 'main_app/publish.html'



class CarEditView(UpdateView):
    model = Car
    fields = ['brand', 'model']  # Поля, которые вы хотите редактировать
    template_name = 'main_app/update.html'  # Шаблон для редактирования машины
    success_url = reverse_lazy('cars')  # URL-адрес для перенаправления после успешного редактирования

class MotoEditView(UpdateView):
    model = Motocycle
    context_object_name = 'car'
    fields = ['brand', 'model']  # Поля, которые вы хотите редактировать
    template_name = 'main_app/update.html'  # Шаблон для редактирования машины
    success_url = reverse_lazy('motos')  # URL-адрес для перенаправления после успешного редактирования



class CarDeleteView(DeleteView):
    model = Car
    extra_context = {'title': 'Confirm Delete'}
    context_object_name = 'item'
    success_url = reverse_lazy('cars')  # URL, на который перенаправлять после успешного удаления машины
    template_name = 'main_app/confirm_delete.html'  # Шаблон для подтверждения удаления

class MotoDeleteView(DeleteView):
    model = Motocycle
    extra_context = {'title': 'Confirm Delete'}
    context_object_name = 'item'
    success_url = reverse_lazy('motos')  # URL, на который перенаправлять после успешного удаления машины
    template_name = 'main_app/confirm_delete.html'  # Шаблон для подтверждения удаления

