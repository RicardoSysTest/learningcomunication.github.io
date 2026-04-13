from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

from . models import Task

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'board/register.html'
    success_url = 'notes/notelist'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'board/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'board/login.html'


class HomeView(TemplateView):
    template_name = 'board/index.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'board/authorized.html'
    login_url = '/admin'
    all_task = Task.objects.all()
    extra_context = {'list_task': all_task}
