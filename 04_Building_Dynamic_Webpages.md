## Buildin Dinamic Webpages



## Creating 
Now that we have our notes, let's create a new view to display them in the same way we created the other one. From notes app open  `views.py` start with importing the models and import notes. Okay, now let's create a function call list that receives a request and then a variable, all_notes that stores all the notes that we have in our database. Now, let's return the render function again, request a template that we're going to create a little bit later, notes/notes_list.html, and now the brackets with notes are equal to all_notes
```py
    from django.shortcuts import render
    from .models import Notes

    def list(request):
        all_notes = Notes.objects.all()
        return render(request, 'notes/notes_list.html',{'notes':all_notes})


    # Create your views here.  
```
This is not much different from what we did in the other view, except for one thing, we are querying for all notes and sending them to the template. This way, when the template is rendered, all the information coming directly from the database will be available. Before we jump to the template, let's organize URLs. 

So let's create a new URLs file here in the notes app and that's going to have the same format. So from django.urls import path. Then let's import the views here, and then the urlpatterns that has a list. Then here, the path, our endpoint's going to call notes because that's the list of notes. Then views.list, which is the function we just created. 
```py
    from django.urls import include, path
    from . import views

    urlpatterns = [
        path('notes', views.list),
    ]
```
The last thing is that we have to add this on the urls.py file on smart notes. So let's add comma here, then path. Let's add smart here, and then include notes.urls.
```py
from django.contrib import admin
from django.urls import include, path

from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("board.urls")),
    path('smart/', include("notes.urls")),
]

```
All the URLs that we are adding on notes.urls will be added after the smart. So smart's going to be a part of that endpoint. This is a really nice way of organizing our project. Okay, almost there. Now we need to create the template folder. So notes, new folder, templates, then a new folder, notes, and now we can add our template. Notes_list.html. 


Okay, now we can create our template. So let's start by html and h1, these are the notes.  And I will start to use the powers of DTL. Bear with me just a little bit. So let's start with ul, and then curly brackets, two percentages, and in the middle, for note in notes. Okay, so in here we're going to add a line item, {{note.title}} close the curly brackets, and now we need to do curly brackets, percentage, percentage, and in the middle it's going to have an endfor.
```html
    <html>
    <h1>These are the notes</h1>
        <ul>
            {% for note in notes %}
            <li>{{note.title}}</li>
            {% endfor %}
        </ul>
    </html>
```
Okay, what's happening here? Everything that is between curly brackets is the django template language logic. Here, we're opening a list tag, ul, and then saying that for each note we receive in the template, DTL should create a list item, the li. Notice that commands such as the loop happen between curly brackets and percentages, while things that should be rendered by the template are between double brackets. So let's save this, then run this, runserver and open it. Okay, now we can see that we have a smart here. Then let's try this smart. We're going to have the notes and here are the notes. There it is, a webpage that is dynamically getting data from the database and adding it to the HTML. If we right click here and inspect the page, we'll see here that we actually have two line items. That's because we have only two nodes on the database. If we had many more, many more would be created. How easy was that? I encourage you now to go and create more notes, either via the shell or the admin and see what happens here.


## Creating yuor first Django Dynamic Webpage (how to create views using functions)
Now that we have a list of notes, we want to create a way to visualize details of a particular note. Let's go back to the notes app, views.py, and create a new function here. Now, this function should receive a second parameter called pk for private key. So let's go def detail(request, pk), okay. Now, we can use this pk to go in the database and get that particular note. So note = Notes.objects.get(pk=pk). Okay, and the common response, return render the request. Let's keep the pattern here, so notes/notes_detail.html, and then let's pass note inside the brackets
```py
    from django.shortcuts import render
    from .models import Notes

# Create your views here.
def list(request):

    # Get all notes store in our DB
    all_notes = Notes.objects.all()

    # Return the render or the template note_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk)
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_detail.html',{'note':note})

```

  . Okay, now, what we need to do is create the template. So let's go back here. New file, notes_detail.html, and let's create a simple html that has the title as note.title as an h1, and then let's go a text here, note.text, and there you go. 
  ```html
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blog</title>
        </head>
        <body>
            <h1>{{ note.title %}}</h1>
            <p>{{note.text}}</p>
        </body>
        </html>
  ```
  
  Okay, so there's one thing still missing, which is the URL. we need to be able to pass down a second parameter to the function adding a new path (open the `urls` file from the application). So we're going to have notes then slash, the minor and greater sign, and pk, great, and, now, the views.detail. 
  ```py

    from django.urls import include, path

    from . import views

    urlpatterns = [
        path('notes', views.list),
        path('notes/<int:pk>',views.detail),
    ]

  ```
  Okay, so what we're telling here is that this URL will receive a new value named pk that will be an integral number. Now, the only thing left to do is start the run server again (keyboard clacks) and test this out. So here, we have the notes, and if we pass now the pk for our first note, we can see the template displaying the details of the first note. Okay, so this works fine, but we still have a problem. The get method that we're using to get the note from the database will actually throw an error if you pass down a private key that doesn't exist. So if we tried the same URL but with, I dunno, 11 or something, unless you have created 11 notes, this will raise an error. So let's try it out. Notice here that this is returning an exception of the type does not exist. We can also see here that there is a message with the exception saying, "Notes matching query does not exist." Django has an amazing traceback for us to understand where exactly the error happened. You can see right here that the problem is started in line 11 on the notes views.py file, which is exactly where we defined the query. We only have this paging explaining the error again because we continue to have the debug equals true in the settings file. In a production environment, the user would see a 500 error, which means an internal error. When an object is not found, the correct response is a 404 status code saying that that object does not exist. So let's change our code to make sure that we get the correct status code. 
  
  Let's go back to the views file, and in here, let's import from django.http. Let's import Http404, okay? And, now, we can wrap this query in a try and except block, so try and except. If the Notes.DoesNotExist equals true, we're going to raise an Http404 with the message "Note doesn't exist." 
  ```py
  from django.shortcuts import render
  from django.http import Http404
  from .models import Notes

  # Create your views here.
  def list(request):

    # Get all notes store in our DB
    all_notes = Notes.objects.all()

    # Return the render or the template note_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


  def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})

  ```
  Okay, so if you go back now to the previous link and refresh, we're going to see here that this page is now returning a 404 with a message that we defined. This is a much nicer flow than the error we had before, because we're controlling the message to the user. If you can, we can actually create another template specifically for a 404 and return it with a nice message. It is completely up to you.


## How can Django  can list data with just some small changes(Class-Based Views.)
  Most views have similar patterns. Class-based views are extensive classes that implement typical view behavior and you just need to override a few things to make it do what you want. Let's go back to our code and change our views that are function-based to the ones that are class-based and see in detail how class-based views work. 
  
  The first view we made was in the Kanban app, so let's go back and change it. The only thing we need to do here is display a template. So we can do that by using the class-based view template view class. So let's in here import from django.views.generic. import TemplateView. 
  ```py
  from django.shortcuts import render
  from django.http import HttpResponse
  from datetime import datetime
  from django.contrib.auth.decorators import login_required
  from django.views.generic import TemplateView

  from . models import Task

  class HomeView(TemplateView):
    template_name = 'board/dashboard.html'
    extra_context = {'today': datetime.today()}

  # Create your views here.
  def board(request):
    return render(request, 'board/Index.html',{'today': datetime.today()} )


  @login_required(login_url='/admin')
  def authorized(request):
    all_task = Task.objects.all()
    return render(request, 'board/authorized.html', {'list_task': all_task})

  ```
  Okay, so now we can create a new class called HomeView that inherits from TemplateView. And the only thing we need to pass here is the template name. So we can copy here and paste it here. And that's it. We still need one more thing because our template requires some extra information. So we can add a variable called extra_context and now pass this dictionary here in it. We can delete this now. Oops, it's missing something. Okay, so now we can delete this function here. 
```py
  from django.shortcuts import render
  from django.http import HttpResponse
  from datetime import datetime
  from django.contrib.auth.decorators import login_required
  from django.views.generic import TemplateView

  from . models import Task

  class HomeView(TemplateView):
    template_name = 'board/dashboard.html'
    extra_context = {'today': datetime.today()}

  @login_required(login_url='/admin')
  def authorized(request):
    all_task = Task.objects.all()
    return render(request, 'board/authorized.html', {'list_task': all_task})

  ```
  The last thing missing is that we need to change the way the URLs are defined in the application. So let's go to the URLs and in here, instead of passing the home function, we're going to pass the home view class.
```py
  from django.urls import path

  # from board import views
  from . import views

  urlpatterns = [
     path('home', views.board),
     path('todolist', views.authorized), 
  ] 
```
And we need to call a method called as_view. You can see here now that the server is working just fine, so we can go back here and it's still working. 
```py
  from django.urls import path

  # from board import views
  from . import views

  urlpatterns = [
     path('home', views.HomeView.as_view()),
     path('todolist', views.authorized), 
  ] 
```
So we can quickly do the same with the second function here, the authorized view. So let's create a class called AuthorizedView that also inherits from TemplateView. Then the template_name, we're going to have this here. 
```py
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.decorators import login_required

from . models import Task

# Create your views here.


class HomeView(TemplateView):
    template_name = 'board/index.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(TemplateView):
    template_name = 'board/authorized.html'
    all_task = Task.objects.all()
    extra_context = {'list_task': all_task}
```
 
Because we don't have the extra attributes required here, we can just not pass the extra content. 

But we're still missing authentication. How do we handle authentication on class-based views? Well, to do that, we're going to need a mixing class. Mixings are helper classes that can be used along with other classes to provide additional features. For this case, we'll use the login required mix in. So let's go back and use t import LoginRequiredMixin. 
```py
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Task

# Create your views here.


class HomeView(TemplateView):
    template_name = 'board/index.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(TemplateView):
    template_name = 'board/authorized.html'
    all_task = Task.objects.all()
    extra_context = {'list_task': all_task}
```
The only thing we need to do here now is make sure that this class, which is a mixin, is added before the template view. Okay, the last thing missing is the login URL. So we can actually go here, add the login_url, that's still pass the admin, and that's it. 
```py
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Task

# Create your views here.
class HomeView(TemplateView):
    template_name = 'board/index.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'board/authorized.html'
    login_url = '/admin'
    all_task = Task.objects.all()
    extra_context = {'list_task': all_task}

```
So we can remove this now, fix the URLs to be AuthorizedView.as_view, 
```py
from django.urls import path

# from board import views
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    #path('todolist', views.),
    path('todolist', views.AuthorizedView.as_view()),
]

```
and that's it. As you can see here, things are quite nice and well organized. And you also don't have to remember the request is coming in and out of the function. Class-based views might not seem like the amazing features they are, but that's because we are still handling simple views. As the views increase in complexity, they become more and more amazing allies.


## Introduction to Django class-based views: A Few classes have the power to change the world
We worked with templates, but now it's time for more complex views. Let's start with our last endpoint. On the notes, let's go to views.py file from notes. And in here, let's import from Django.views.generic import ListView. 
```py
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView

# Create your views here.


def list(request):

    # Get all notes store in our DB
    all_notes = Notes.objects.all()

    # Return the render or the template note_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})

```

Okay, now we can start our class-based view. Let's go to create a class. So let's call it NotesListView that inherits from ListView. And we need to add here which model we're listing objects from. So let's add here Model = Notes. Okay. And because our template is expecting to receive a list called Notes, we should also add here that the context object name is different from the default. The default is objects, but we call it notes. That's it, that's our whole endpoint. 
```py
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView

# Create your views here.
class NoteListView(ListView):
    # List objects from Notes model
    model = Notes
    # Call the conect object name that is different from the default
    context_object_name = 'notes'

def list(request):

    # Get all notes store in our DB
    all_notes = Notes.objects.all()

    # Return the render or the template note_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})

```
The only thing we need to do now is change the endpoint URL (Open the `urls.py` from notes). So let's go back here, then change list to NotesListView.as view, and that's it. 
```py
    from django.urls import include, path

    from . import views

    urlpatterns = [
        #path('notes', views.list),
        path('notes', views.NotesListView.as_view()),
        path('notes/<int:pk>', views.detail),
    ]

```
 We can go back here and also delete our old endpoint.
```py
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView

# Create your views here.
class NoteListView(ListView):
    # List objects from Notes model
    model = Notes
    # Call the conect object name that is different from the default
    context_object_name = 'notes'

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
```
Instead of homes, we're going to go to smart notes. The list view is already making the query for us. We also don't need to define a template name because we created a template name that follows the standard of that class-based view. But if we add a different name, it might not work. So instead we can pass here an attribute called template name.
```py
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView

# Create your views here.
class NoteListView(ListView):
    # List objects from Notes model
    model = Notes
    # Call the conect object name that is different from the default
    context_object_name = 'notes'
    template_name = "notes/notes_list.html"

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
```
 You guessed it correctly. So we can say here, notes notes_list.html. Yeah, that's all we have to do for the list endpoint. 
 
 For the detail view we need to just import the `DetailView` and create the `class NotesDetailView` that inherits `from DetailView`. Here we need `model = notes` and  `context_object_name = note` 
 ```py
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView, DetailView

# Create your views here.
class NoteListView(ListView):
    # List objects from Notes model
    model = Notes
    # Call the conect object name that is different from the default
    context_object_name = 'notes'
    template_name = "notes/notes_list.html"

class DetailView(DetailView):
    model = Notes
    context_object_name = 'note'
 ```
 What about the exception we throw when the object can't be found?" There's no need. The detail class-based view already take care of that for us. There is no need for us to handle any of that complexity.  Let's change URL and give it a try. So in here, let's change `views.detail` for `views.NotesDetailView.as_view()`.
 ```py
    from django.urls import include, path

    from . import views

    urlpatterns = [
        #path('notes', views.list),
        path('notes', views.NotesListView.as_view()),
        path('notes/<int:pk>', views.NotesDetailView.as_view()),
    ]

```
 
  And if we go to something that doesn't exist, yep, it's still returning a 404. Hopefully at this point you can already see how class-based views are an amazing feature of Django and we've only scratched the surface. There are very few case scenarios where you will prefer to create a function-based view as the ones you just replaced. In the vast majority of cases, a class-based view will be the ideal tool for you.