from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView

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
    extra_context = {'title': 'Создать объявление'}
    login_url = 'register:login'
    vehicle = 'sdf'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = self.vehicle
        return context




AddCar = type('AddCar', (AddItem,), {'form_class': CarForm, 'vehicle': 'автомобиль'})
AddMoto = type('AddMoto', (AddItem,), {'form_class': MotocycleForm, 'vehicle': 'мотоцикл'})
AddService = type('AddService', (AddItem,), {'form_class': ServiceForm, 'vehicle': 'услуга'})



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
