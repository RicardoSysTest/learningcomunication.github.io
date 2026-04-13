from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/notelist'
    template_name = 'notes/notes_delete.html'
    login_url = 'login'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes/notelist'
    form_class = NotesForm
    login_url = 'login'


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/notelist'
    form_class = NotesForm
    login_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notelist'
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'notes'
    login_url = 'login'
