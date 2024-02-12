from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from .forms import AddCarForm
from .models import *


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
