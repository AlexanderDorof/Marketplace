from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.generic.edit import FormView


@login_required
def profile_view(request):
    return render(request, 'profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy("register:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)