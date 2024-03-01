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
