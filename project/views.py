from django.shortcuts import render
from django.views.generic import ListView
from .models import Projects
# Create your views here.


class ProjectListView(ListView):
    model = Projects
    context_object_name = 'project'


def project(request):
    return render(request, 'project/project.html', {})
