from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from icecream import ic

from .forms import UserRegistrationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


@login_required
def profile_view(request):
    return render(request, 'register/profile.html')


class RegisterView(FormView):

    form_class = UserRegistrationForm
    template_name = 'register/register.html'
    success_url = reverse_lazy("register:profile")

    def form_valid(self, form):
        password = form.cleaned_data['password']
        form.save(password=password)
        return super().form_valid(form)
