from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


@login_required
def profile_view(request):
    return render(request, 'profile.html')


class RegisterView(FormView):
    # form_class = UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)