from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from asgiref.sync import sync_to_async
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .utils import *


def index(request):
    context = funcmixin(request, title='Главная страница')
    return render(request, 'main_app/index.html', context=context)


def info(request):
    context = funcmixin(request, title='О магазине')
    return render(request, 'main_app/info.html', context=context)


async def add_to_favorite(request):

    def get_current_user():
        return User.objects.get(user_django__pk=request.user.pk)

    def favorite_cars_by_item_pk(user, item_pk):
        return user.favorite.favorite_cars.filter(pk=item_pk).exists()
    def favorite_motos_by_item_pk(user, item_pk):
        return user.favorite.favorite_moto.filter(pk=item_pk).exists()

    def car_by_item_pk(item_pk):
        return Car.objects.get(pk=item_pk)

    def car_add_to_favorite(user, instance):
        user.favorite.favorite_cars.add(instance)

    def car_remove_from_favorite(user, instance):
        user.favorite.favorite_cars.remove(instance)


    def moto_by_item_pk(item_pk):
        return Motocycle.objects.get(pk=item_pk)

    def moto_add_to_favorite(user, instance):
        user.favorite.favorite_moto.add(instance)

    def moto_remove_from_favorite(user, instance):
        user.favorite.favorite_moto.remove(instance)

    item_pk = request.GET.get('pk')
    item_type = request.GET.get('vehicle')
    user = await sync_to_async(get_current_user)()
    if item_type == 'car':
        car_instance = await sync_to_async(car_by_item_pk)(item_pk)
        car_in_favorite = await sync_to_async(favorite_cars_by_item_pk)(user, item_pk)
        if not car_in_favorite:
            await sync_to_async(car_add_to_favorite)(user, car_instance)
        else:
            await sync_to_async(car_remove_from_favorite)(user, car_instance)
    elif item_type == 'motocycle':
        moto_instance = await sync_to_async(moto_by_item_pk)(item_pk)
        moto_in_favorite = await sync_to_async(favorite_motos_by_item_pk)(user, item_pk)
        if not moto_in_favorite:
            await sync_to_async(moto_add_to_favorite)(user, moto_instance)
        else:
            await sync_to_async(moto_remove_from_favorite)(user, moto_instance)

    return JsonResponse({'image': '/static/static_imgs/heart-icon.svg', 'pk': item_pk})


def contacts(request):
    context = funcmixin(request, title='Контакты')
    return render(request, 'main_app/contacts.html', context=context)


class FavoriteList(LoginRequiredMixin, DataMixin, PaginationMixin, ListView):
    extra_context = {'title': 'Избранное', 'item_name': 'main_app/vehicle.html'}
    template_name = 'main_app/cards.html'
    login_url = 'register:login'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        # send_email_task.delay('message get')
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        context['items'] = self.paginated_object(queryset=self.get_queryset())
        context['page_range'] = self.paginate_page_range(total_pages=context['items'].paginator.num_pages,
                                                         page_number=context['items'].number)
        return context

    def get_queryset(self):
        djangouser = self.request.user
        user = User.objects.get(user_django=djangouser)
        fav = user.favorite
        cars = list(fav.favorite_cars.all())
        motos = list(fav.favorite_moto.all())
        return cars + motos


def pageNotFoundRedirect(request, exception):
    context = funcmixin(request, title='Страница не найдена')
    return render(request, 'main_app/404.html',context=context, status=404)