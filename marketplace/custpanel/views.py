from django.contrib.auth.decorators import user_passes_test
from django.db.models import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from icecream import ic
from queryset_sequence import QuerySetSequence

from .forms import *
from .permissions import AdminPermissionsMixin, user_is_admin
from .utils import PaginationMixin


@user_passes_test(test_func=user_is_admin, login_url='register:login')
def admin_home(request):
    context = {'title': 'Панель администратора'}
    return render(request, 'custpanel/index.html', context=context)


# CREATE

class AddItem(AdminPermissionsMixin, CreateView):
    form_class = CarForm
    template_name = 'custpanel/create.html'
    extra_context = {'title': 'Создать объявление', 'vehicle': 'автомобиль'}
    login_url = 'register:login'
    success_url = reverse_lazy('admin-panel:admin_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = self.vehicle
        return context

    def get_initial(self):
        initial = super().get_initial()
        pk = self.request.user.pk
        user = User.objects.get(user_django__pk=pk)
        initial['seller'] = user
        initial['used_car'] = True
        return initial


AddCar = type('AddCarz', (AddItem,), {'form_class': CarForm, 'vehicle': 'автомобиль'})
AddMoto = type('AddMoto', (AddItem,), {'form_class': MotocycleForm, 'vehicle': 'мотоцикл'})
AddService = type('AddService', (AddItem,), {'form_class': ServiceForm, 'vehicle': 'услуга'})


class VehicleDeleteView(AdminPermissionsMixin, DeleteView):
    model = Car
    extra_context = {'title': 'Подтвердить удаление'}
    context_object_name = 'item'
    success_url = reverse_lazy('admin-panel:admin_home')  # URL-name, redirected after successful deletion
    template_name = 'custpanel/confirm_delete.html'  # Template for confirmation deletion


CarDeleteView = type('CarDeleteView', (VehicleDeleteView,), {'model': Car})
MotoDeleteView = type('MotoDeleteView', (VehicleDeleteView,),
                      {'model': Motocycle})
ServiceDeleteView = type('CarDeleteView', (VehicleDeleteView,), {'model': Service})

@user_passes_test(test_func=user_is_admin, login_url='register:login')
def delete(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        motocycles = Motocycle.objects.all()
        services = Service.objects.all()
        users = User.objects.all()
        context = {'title': 'Удалить записи', 'items': [cars, motocycles, services, users]}

    if request.method == 'POST':
        request_dict = dict(request.POST)
        car_ids = request_dict.get('car', None)
        motorcycle_ids = request_dict.get('motocycle', None)
        service_ids = request_dict.get('service', None)
        user_ids = request_dict.get('user', None)
        cars = Car.objects.filter(pk__in=car_ids) if car_ids else Car.objects.none()
        motorcycles = Motocycle.objects.filter(pk__in=motorcycle_ids) if motorcycle_ids else Motocycle.objects.none()
        services = Service.objects.filter(pk__in=service_ids) if service_ids else Service.objects.none()
        users = User.objects.filter(pk__in=user_ids) if user_ids else User.objects.none()
        query = QuerySetSequence(cars, motorcycles)
        query = QuerySetSequence(query, services)
        query = QuerySetSequence(query, users)
        query.delete()
        return redirect('admin-panel:delete')


    return render(request, 'custpanel/delete.html',
                  context=context)


class ItemEditView(AdminPermissionsMixin, UpdateView):
    extra_context = {'title': 'Редактирование записи'}
    template_name = 'custpanel/change.html'
    form_class = CarForm
    context_object_name = 'item'


CarEditView = type('CarEditView', (ItemEditView,), {'model': Car})
MotoEditView = type('MotoEditView', (ItemEditView,),
                    {'model': Motocycle, 'form_class': MotocycleForm})
ServiceEditView = type('ServiceEditView', (ItemEditView,), {'model': Service, 'form_class': ServiceForm})


# display from db
class VehicleList(AdminPermissionsMixin, PaginationMixin, ListView):
    template_name = 'custpanel/list.html'
    paginate_by = 20
    item_name = 'custpanel/list/list-cars.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['item_name'] = self.item_name
        context['items'] = self.paginated_object(self.model.objects.all().order_by('id'))
        context['page_range'] = self.paginate_page_range(total_pages=context['items'].paginator.num_pages,
                                                         page_number=context['items'].number)

        return context


CarsList = type('CarsList', (VehicleList,), {'model': Car, 'title': 'Каталог машин'})
MotorcyclesList = type('MotosList', (VehicleList,), {'model': Motocycle, 'title': 'Каталог мотоциклов',
                                                     'item_name': 'custpanel/list/list-motorcycles.html'})
ServicesList = type('ServicesList', (VehicleList,),
                    {'model': Service, 'title': 'Услуги', 'item_name': 'custpanel/list/list-services.html'})
