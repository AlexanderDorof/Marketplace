from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from main_app.forms import AddCarForm, AddMotoForm
from main_app.models import *
from main_app.utils import *
from main_app.permissions import AuthorPermissionsMixin


# READ

class VehicleList(DataMixin, PaginationMixin, ListView):
    template_name = 'main_app/cards.html'
    paginate_by = 12
    item_name = 'main_app/vehicle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['item_name'] = self.item_name
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        context['items'] = self.paginated_object(self.model.objects.all().order_by('id'))

        page_number = context['items'].number
        num_pages = context['items'].paginator.num_pages

        context['page_range'] = [1]  # Всегда добавляем первую страницу

        # Определяем диапазон страниц в зависимости от текущей страницы
        if num_pages <= 7:
            context['page_range'] += list(range(2, num_pages + 1))
        elif page_number <= 3:
            context['page_range'] += list(range(2, 5))
            context['page_range'] += [None, num_pages]
        elif page_number >= num_pages - 2:
            context['page_range'] += [None, num_pages - 3]
            context['page_range'] += list(range(num_pages - 2, num_pages + 1))
        else:
            context['page_range'] += [None, page_number - 2, page_number - 1, page_number]
            context['page_range'] += list(range(page_number + 1, page_number + 3))
            context['page_range'] += [None, num_pages]

        return context


CarsList = type('CarsList', (VehicleList,), {'model': Car, 'title': 'Каталог машин'})
MotosList = type('MotosList', (VehicleList,), {'model': Motocycle, 'title': 'Каталог мотоциклов'})
ServicesList = type('ServicesList', (VehicleList,),
                    {'model': Service, 'title': 'Услуги', 'item_name': 'main_app/service.html'})


class ItemDetailView(DataMixin, DetailView):
    template_name = 'main_app/item_description.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание товара'
        context['edit_ref'] = self.edit_ref
        context['delete_ref'] = self.delete_ref
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


CarDetailView = type('CarDetailList', (ItemDetailView,),
                     {'model': Car, 'edit_ref': 'edit_car', 'delete_ref': 'delete_car'})
MotoDetailView = type('MotoDetailView', (ItemDetailView,),
                      {'model': Motocycle, 'edit_ref': 'edit_moto', 'delete_ref': 'delete_moto'})
ServiceDetailView = type('MotoDetailView', (ItemDetailView,), {'model': Service, 'title': 'Описание услуги',
                                                               'template_name': 'main_app/service_description.html'})


# CREATE

class AddItem(LoginRequiredMixin, DataMixin, CreateView):
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


AddCar = type('AddCar', (AddItem,), {'form_class': AddCarForm})
AddMoto = type('AddMoto', (AddItem,), {'form_class': AddMotoForm, 'vehicle': 'мотоцикл'})


# UPDATE

class ItemEditView(AuthorPermissionsMixin, DataMixin, UpdateView):
    extra_context = {'title': 'Редактирование записи'}
    fields = "__all__"
    template_name = 'main_app/update.html'

    # success_url = reverse_lazy('cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_auth_mixin = self.get_user_context()
        context = {**context, **user_auth_mixin}
        return context


CarEditView = type('CarEditView', (ItemEditView,), {'model': Car, 'success_url': reverse_lazy('cars')})
MotoEditView = type('MotoEditView', (ItemEditView,), {'model': Motocycle, 'success_url': reverse_lazy('motos')})


# DELETE

class VehicleDeleteView(AuthorPermissionsMixin, DataMixin, DeleteView):
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


CarDeleteView = type('CarDeleteView', (VehicleDeleteView,), {'model': Car, 'success_url': reverse_lazy('cars')})
MotoDeleteView = type('MotoDeleteView', (VehicleDeleteView,),
                      {'model': Motocycle, 'success_url': reverse_lazy('motos')})
