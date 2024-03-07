from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView

from .forms import *
from .utils import PaginationMixin


def admin_home(request):
    context = {'title': 'Панель администратора'}
    return render(request, 'custpanel/index.html', context=context)


def create(request):
    form = CarForm()
    motocycle_form = MotocycleForm()
    service_form = ServiceForm()
    user_form = UserForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        motocycle_form = MotocycleForm(request.POST)
        service_form = ServiceForm(request.POST)
        user_form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_home')

        if motocycle_form.is_valid() and 'Motocycle_create' in request.POST:
            motocycle_form.save()
            return redirect('admin_home')

        if service_form.is_valid() and 'Service_create' in request.POST:
            service_form.save()
            return redirect('admin_home')

        if user_form.is_valid() and 'User_create' in request.POST:
            user_form.save()
            print("User created successfully!")  # Отладочное сообщение
            return redirect('admin_home')
        else:
            print("User form is not valid:", user_form.errors)  # Отладочное сообщение об ошибке

    return render(request, 'custpanel/create.html',
                  {'form': form, 'motocycle_form': motocycle_form, 'service': service_form, 'user': user_form})


def delete(request):
    if request.method == 'POST':
        # Проверяем, к какой модели относится запрос
        model_type = request.POST.get('model_type', None)

        if model_type == 'car':
            model_id = request.POST.get('car')
            model = get_object_or_404(Car, id=model_id)
        elif model_type == 'motocycle':
            model_id = request.POST.get('motocycle')
            model = get_object_or_404(Motocycle, id=model_id)
        elif model_type == 'service':
            model_id = request.POST.get('service')
            model = get_object_or_404(Service, id=model_id)
        elif model_type == 'user':
            model_id = request.POST.get('user')
            model = get_object_or_404(User, id=model_id)
        else:
            # Возможно, добавьте дополнительные обработки, если это необходимо
            pass

        model.delete()
        return redirect('admin_home')

    cars = Car.objects.all()
    motocycles = Motocycle.objects.all()
    service = Service.objects.all()
    users = User.objects.all()

    return render(request, 'custpanel/delete.html',
                  {'cars': cars, 'motocycles': motocycles, 'service': service, 'users': users})


def change(request):
    if request.method == 'POST':
        if 'car' in request.POST:
            car_id = request.POST.get('car')
            car = get_object_or_404(Car, id=car_id)

            form = CarForm(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
        elif 'motocycle' in request.POST:
            motocycle_id = request.POST.get('motocycle')
            motocycle = get_object_or_404(Motocycle, id=motocycle_id)

            motocycle_form = MotocycleForm(request.POST, instance=motocycle)
            if motocycle_form.is_valid():
                motocycle_form.save()
                return redirect('admin_home')

        elif 'service' in request.POST:
            service_id = request.POST.get('service')
            service = get_object_or_404(Service, id=service_id)

            service_form = ServiceForm(request.POST, instance=service)
            if service_form.is_valid():
                service_form.save()
                return redirect('admin_home')

        elif 'user' in request.POST:
            user_id = request.POST.get('user')
            user = get_object_or_404(User, id=user_id)

            user_form = UserForm(request.POST, instance=user)
            if user_form.is_valid():
                user_form.save()
                return redirect('admin_home')


    else:
        cars = Car.objects.all()
        form = CarForm()
        motocycles = Motocycle.objects.all()
        motocycle_form = MotocycleForm()
        service = Service.objects.all()
        service_form = ServiceForm()
        user = User.objects.all()
        user_form = UserForm()

    return render(request, 'custpanel/change.html',
                  {'cars': cars, 'motocycles': motocycles, 'form': form, 'motocycle_form': motocycle_form,
                   'service': service, 'service_form': service_form, 'user': user, 'user_form': user_form})

# display from db
class VehicleList(PaginationMixin, ListView):
    template_name = 'custpanel/list.html'
    paginate_by = 20
    # item_name = 'main_app/vehicle.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        # context['item_name'] = self.item_name
        context['items'] = self.paginated_object(self.model.objects.all().order_by('id'))
        context['page_range'] = self.paginate_page_range(total_pages=context['items'].paginator.num_pages,
                                                         page_number=context['items'].number)

        return context


CarsList = type('CarsList', (VehicleList,), {'model': Car, 'title': 'Каталог машин'})
MotosList = type('MotosList', (VehicleList,), {'model': Motocycle, 'title': 'Каталог мотоциклов'})
ServicesList = type('ServicesList', (VehicleList,),
                    {'model': Service, 'title': 'Услуги', 'item_name': 'main_app/service.html'})


def list(request):
    cars = Car.objects.all()
    # Предположим, что вы хотите отображать по 10 автомобилей на странице
    paginator = Paginator(cars, 10)
    # Получите номер страницы из параметра запроса, или используйте 1, если он не предоставлен
    page_number = request.GET.get('page', 1)
    # Получите объект страницы для текущего номера страницы
    cars_page = paginator.get_page(page_number)

    motocycles = Motocycle.objects.all()
    motocycles_paginator = Paginator(motocycles, 10)
    motocycles_page_number = request.GET.get('motocycles_page', 1)
    motocycles_page = motocycles_paginator.get_page(motocycles_page_number)

    service = Service.objects.all()
    service_paginator = Paginator(service, 10)
    service_page_number = request.GET.get('service_page', 1)
    service_page = service_paginator.get_page(service_page_number)

    user = User.objects.all()
    users_paginator = Paginator(user, 10)
    users_page_number = request.GET.get('users_page', 1)
    users_page = users_paginator.get_page(users_page_number)

    return render(request, 'custpanel/list.html',
                  {'cars': cars, 'motocycles': motocycles, 'service': service, 'user': user, 'cars_page': cars_page,
                   'motocycles_page': motocycles_page, 'service_page': service_page, 'users_page': users_page})
