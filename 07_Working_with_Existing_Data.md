## The U in the CRUD: Updating data
Okay, so now, we have the create endpoint. It's time to create the U update endpoint. Let's go back to the views file on notes. And on here, we're going to also add UpdateView. Now, we can add a new class, NotesUpdateView that inherits from UpdateView. And we actually just need to copy this from the create view and paste it here. That's it. That's all we need to do.

```py

from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Notes
from .forms import NotesForm

# Create your views here.
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/note/noteslist'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/note/noteslist'
    form_class = NotesForm


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notelist'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


```
The only thing still missing are the URLs. So what we can do is go back here. We can copy and paste the details view, and then add here a slash edit on the endpoint. Change the class, whereas this originating to, and the name. That's it. That's all we need to do. If we go back to the notes now, get the first note and then add a slash edit at the end. 

```py
"""
URL configuration for kanban project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from . import views

urlpatterns = [
    path('notelist', views.NoteListView.as_view(), name="notes.list"),
    path('<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
    path('<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('new', views.NotesCreateView.as_view(), name="notes.new"),
]

```

You can see that we have our form here, and we have the fields already filled in with the data from that particular note. So if we try something, just save and try again. Uh-oh, it didn't work. Okay, so let's check it out what is going on. If you go to our template, if you notice here, we're actually hard coding, which URL the form should be sent to. 

```html
{% extends 'base.html'%} {%block content%}
<form action="{% url 'notes.new' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">{{form.errors.title.as_text}}</div>
{% endif%} {% endblock %}

```

We don't actually need this. The form is smart enough to know where to send this to. So let's get rid of this. 
```html
{% extends 'base.html'%} {%block content%}
<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">{{form.errors.title.as_text}}</div>
{% endif%} {% endblock %}

```
Let's go back, edit, and then submit it. If we see now, our note was edited. That's it. So editing basically comes for free after you implemented the create endpoint. we can style this page a little bit. So let's go to the template. We can add a cancel button that will return from this page if the user changed their mind. So it can go to a, href, it's going to be the function that have URL, and then this go back to notes.list. We still need some class here, so let's tie button and then button secondary and then cancel. 

```html
{% extends 'base.html'%} {%block content%}
<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">{{form.errors.title.as_text}}</div>
{% endif%}
<a href="{% url 'notes.list' %}" class="btn btn-secondary">Cancel</a>
<a href="{% url 'notes.update' pk=note.id %}" class="btn btn-secondary">Edit</a>
{% endblock %}


```

We can also go back to the details. In here, we can create a new button that will take us to the added page, so a, the href, then curly brackets, percentage, URL, notes.update, and then PK is equal to note.id. Let's add some class here as well, so btn and btn secondary, edit. Okay, let's try this out. If we go back here and this note, we now have the button edit. We can actually edits here and then we can actually cancel or submit. There you go. Now, you have a full cycle between list, detail, and edit, with just a couple lines of code.


## The D in the CRUD: Deleting data
From the CRUD operations, deleting data. Go back to the views. And from here, we're going to add `from django.views.generic.edit` and `import DeleteView`. 

```py
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Notes
from .forms import NotesForm

# Create your views here.

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/note/noteslist'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/note/noteslist'
    form_class = NotesForm


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notelist'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

```

The delete endpoint is even simpler than all the endpoints we created until now. We can add a new class, NotesDeleteView, that inherits from DeleteView, and we actually just need the model and a success_url. 
```py
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Notes
from .forms import NotesForm

# Create your views here.
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/note/noteslist'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/note/noteslist'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/note/noteslist'
    form_class = NotesForm


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notelist'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

```

Once more, the endpoint URL need to be added to the urls file. So let's go back here, let's copy this. And instead of edit, let's call this delete. Let's change the class here and the name. Now, we need to create a template to confirm if the user wants to delete a particular note. 
```py
"""
URL configuration for kanban project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from . import views

urlpatterns = [
    path('notelist', views.NoteListView.as_view(), name="notes.list"),
    path('<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
    path('<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('new', views.NotesCreateView.as_view(), name="notes.new"),
]

```

Let's go here and add a new one called `notes_delete.html`. So let's start with the basic `{% extends 'base.html' %}`, then `{% block content%} {% endblock %}`. This is also going to be a form. So let's add form and the method's going to be post `<form method='post'> </form>`. Since this is a form, we can't forget about the `{% csrf_token %}`. And then in here, we're going to add a message,`<p>Are you sure you want to delete?</p>`. And then let's add `"{{notes.title}}"` and then another message, saying that `<p>this action actually can't be undone</p>`. Finally add  `<input type="submit class="btn btn-danger" value="Confirm"/>`

```html
{% extends 'base.html'%}

{% block content %}
    <form method='post'>
        {% csrf_token %}
        <p>Are you sure you want to delete "{{notes.title}}"?</p>
        <p>This action can't be undone</p>

        <input type="submit" class="btn btn-danger" value="confirm"/>
    </form>
{% endblock %}
```

Since we already have our template, we can go back to the details and add yet one more button here that will lead us to the delete. Let's make it red as well. Okay, it's time to try it out. Let's go back to one particular note. 
```py

{% extends "base.html" %} {% block content %}
<div class="border rounded">
  <h1 class="my-5">{{note.title}}</h1>
  <p>{{note.text}}</p>

  <div class="border border-0 p-2">
    <a href="{% url 'notes.list' %}" class="btn btn-secondary btn-lg me-md-2">Back</a>
    <a href="{% url 'notes.update' pk=note.id %}" class="btn btn-secondary btn-lg me-md-2">Edit</a>
    <a href="{% url 'notes.delete' pk=note.id %}" class="btn btn-danger btn-lg me-md-2">Delete</a>
  </div>
  {% endblock %}
</div>


```
Now we have the Delete button. And if we click here, uh-oh, okay, we're getting, again, a template does not exist. We can see here that while it was loading the template, it was looking for a template with the name notes/notes_confirm_delete. So we have two alternatives here. One is to change the name of our template to match the template that Django is expecting. I prefer to usually add the template_name to avoid having to remember which template is related to which endpoint. So we can come back here to the views and add a template_name. 
```py

```
This name is also very similar to the other template_names that we have. So in my opinion, this is a little bit better, but you can choose whatever you prefer. Let's try again. Let's delete this. Okay, we have our message. Let's Confirm. And there you go, the note was deleted.