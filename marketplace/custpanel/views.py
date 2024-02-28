from .models import *
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

def models(request):
    car_form = CarForm()
    return render(request, 'custpanel/models.html', {'car_form': car_form})


def create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        motocycle_form = MotocycleForm(request.POST)
        service = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('models')

        if motocycle_form.is_valid() and 'Motocycle_create' in request.POST:
            motocycle_form.save()
            return redirect('models')

        if service.is_valid() and 'Service_create' in request.POST:
            service.save()
            return redirect('models')

    else:
        form = CarForm()
        motocycle_form = MotocycleForm()
        service = ServiceForm

    return render(request, 'custpanel/create.html', {'form': form, 'motocycle_form': motocycle_form, 'service': service})




def delete(request):
    if request.method == 'POST':
        # Проверяем, к какой модели относится запрос
        if 'car' in request.POST:
            model_id = request.POST.get('car')
            model = get_object_or_404(Car, id=model_id)
        elif 'motocycle' in request.POST:
            model_id = request.POST.get('motocycle')
            model = get_object_or_404(Motocycle, id=model_id)
        else:
            # Возможно, добавьте дополнительные обработки, если это необходимо
            pass

        model.delete()
        return redirect('models')

    cars = Car.objects.all()
    motocycles = Motocycle.objects.all()

    return render(request, 'custpanel/delete.html', {'cars': cars, 'motocycles': motocycles})






def change(request):
    if request.method == 'POST':
        if 'car' in request.POST:
            car_id = request.POST.get('car')
            car = get_object_or_404(Car, id=car_id)

            form = CarForm(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return redirect('models')
        elif 'motocycle' in request.POST:
            motocycle_id = request.POST.get('motocycle')
            motocycle = get_object_or_404(Motocycle, id=motocycle_id)

            motocycle_form = MotocycleForm(request.POST, instance=motocycle)
            if motocycle_form.is_valid():
                motocycle_form.save()
                return redirect('models')
    else:
        cars = Car.objects.all()
        motocycles = Motocycle.objects.all()
        form = CarForm()
        motocycle_form = MotocycleForm()

    return render(request, 'custpanel/change.html', {'cars': cars, 'motocycles': motocycles, 'form': form, 'motocycle_form': motocycle_form})


def list(request):
        new = Car.objects.all()
        motocycles = Motocycle.objects.all()
        return render(request, 'custpanel/list.html', {'news': new, 'motocycles': motocycles})




