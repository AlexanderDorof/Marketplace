from .models import *
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

def car_models(request):
    car_form = CarForm()
    return render(request, 'custpanel/car_models.html', {'car_form': car_form})


def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_models')  # После создания машины возвращаемся к списку
    else:
        form = CarForm()  # При GET запросе создаем пустую форму

    return render(request, 'custpanel/car_create.html', {'form': form})





def car_delete(request):
    if request.method == 'POST':
        # Получите значения из формы (например, car_id)
        car_id = request.POST.get('car')

        # Ищем автомобиль по значению
        car = get_object_or_404(Car, id=car_id)

        # Удаление автомобиля
        car.delete()

        return redirect('car_models')  # Перенаправляем на страницу со списком машин

    else:
        # Если это GET-запрос, отображаем форму выбора модели для удаления
        cars = Car.objects.all()  # Получаем список всех машин
        return render(request, 'custpanel/car_delete.html', {'cars': cars})

# views.py


def car_change(request):
    if request.method == 'POST':
        car_id = request.POST.get('car')
        car = get_object_or_404(Car, id=car_id)

        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_models')
    else:
        cars = Car.objects.all()
        form = CarForm()

    return render(request, 'custpanel/car_change.html', {'cars': cars, 'form': form})




def book_list(request):
    return render(request, 'custpanel/custom.html',)

