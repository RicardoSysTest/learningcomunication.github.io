## Django Forms

## Create a webpage
Whenever we're building a system, there's a couple of common operations that we should support for every model we create. These are: 
* Create 
* Read 
* Update
* Delete
 
Those are the CRUD operations. These are the minimal operations that a system should typically support. So far regarding the notes model, we implemented the retrieve method by having an endpoint to get the details of a particular note. To fully support the notes model, we need to handle all the other three operations as well. Now we're going to learn how to implement a create method. 

Let's go back to notes, views.py, and in here, let's import, well, I hope you guess it, CreateView. Once we have this, we can actually start our new class. So class NotesCreateView that inherits from CreateView. 
```py
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes

# Create your views here.


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

```

And we're going to need three things here. So model = Notes, fields which is going to be ['title', 'text']. And finally, a success_url. That is going to be the '/smart/notes' which is our list endpoint. Let's understand what's going on here. First the model. So the endpoint understands what is regarding to. Then the fields will be the attributes from the model that we allow a user to fill. Since we don't need to pass a created add field, we just define it as title and text. Finally, we want to redirect the user to the list of existing notes so they can see the note they just created. This is the success_url attribute here. And that's it. That's all we need to do in this class. 
```py
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes

# Create your views here.
class NotesCreateView(CreateView):
    model =  Notes
    field = ['title', 'text']
    success_url = '/smart/notes'

class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

```

Now we can add the endpoint to the urls.py file, the same way we did to every other endpoint so far. So in here, let's add path 'notes/new', and then we can call views.NotesCreateView.as_view(). And let's not forget to pass a name to it. So "notes.new", and a comma here. 
```py
from django.urls import include, path

from . import views

urlpatterns = [
    path('notes/notelist', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
    path('notes/new',views.NotesCreateView.as_view(), name="notes.new"),
]

```

Okay, so the last thing that's missing is the template. So let's create it. Let's call it notes_form.html. Okay, so let's use the default template. So extends 'base.html' and then the block content, and finally, the endblock. Okay, so now we can start. To send information back to the server, we'll need a form tag from the HTML. So let's add this here. Okay, so in the form we can do action is equal to, we're going to use the method url and then notes.new, which is the endpoint we just created. And also the method here needs to be POST because we're sending information back to the server. Okay, so now what we need is to allow a user to pass back the information we defined on our endpoint, title and text. How do we do that? Well, this can't be more simple. In here, we can do double curly brackets then form, and that's it. Want to see what happens here? Let's go back to the browser and try out our new endpoint.
```html
{% extends 'base.html'%}

{%block content%}
<form action="{url 'notes.new'}" method='POST'>
    {{ form }}
</form>
{% endblock %}
```

 So in here we can open the inspector element. And you can see here that in the body we have a form, and the form is actually passed down to the HTML as two label tags, and one input tag and one text area. This is because Django already knows which type of data each attribute expects. Thus it creates an appropriate HTML tag to receive it. Well, we're still missing the submit button, so let's add that. So in here, let's add button type="submit." The class is going to be ="btn btn-primary." Let's add some vertical alignment, Submit. That's it. 
 ```html
 {% extends 'base.html'%} {%block content%}
<form action="{url 'notes.new'}" method="POST">
  {{ form }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>
{% endblock %}
 ```
 
 
 Now we have everything we need in place. That is basically all we have to do to have an endpoint to create a new note.

## Understanding how Django Handles Security in POSTs
We did everything we needed to do to implement the create endpoint. But if you try to create a new note, you'll notice that it will actually return a 403 error, meaning that we are forbidden to do this action. Well, we're actually missing one less thing to our form. So if you go here, we can add {%, and then a csrf_token, and that's it. 
```html
{% extends 'base.html'%} {%block content%}
<form action="{url 'notes.new'}" method="POST">
  {% csrf_token %} {{ form }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>
{% endblock %}

```

So let's try again. We can go back. Refresh this page. So this is a new note. It worked. Let's submit. And yes, indeed it works. You're probably wondering, what is this magic that was missing? This is a CSRF token. That stands for Cross-Site Requests Forgery. What happens here is that every time a browser requests a webpage that has a form, Django will send a unique token to that browser. This token will be securely kept and no other website can access it. When the user sends back a form, it'll also send back the token, allowing Django to know that this request is coming from a legit user. Django will then process the request and return the appropriate response. However, if for some reason a third party have access to the user credentials, when they try to make the request from another browser, they won't have the token. So Django understand that this request is coming from an unreliable source and will not process the request, thus, preventing this type of attack. As you can see, this is an additional layer of security that Django is adding to your website with just a small line of code. Beyond the numerous features that allow you to speed up the process of creating a website, these security features are a big part of why developers choose Django to work with.

## Django forms: Powerfil validation with minimal Work
Adding a new endpoint was nice and easy, but now it's time to consider more complex scenarios. Model forms are the best way of doing this in Django. First we're going to create a file called `forms.py` inside our motes app folder. 

Here, let's add:
```py
from django import forms 
from .models import Notes

```

With this, we can create a new class called NotesForm that's going to inherit from forms.ModelForm, and inside this class, we're going to create a new class, Meta. That's going to receive model, which is Notes, and fields, just like we added on the class-based view for Create View.
```py
from django import forms 
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
```

With this we can come back to the `views.py` file, and in here, instead of passing the fields, we're going to pass a `form_class`. That's going to be our NotesForm. We also need to import **it**
```py
from django.shortcuts import render
from django.http import **Http404**
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/notes/notelist'
    form_class = NotesForm


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

``` 
So far what we did will result in exactly the same behavior as we have so far, but the form will give us power to do much more. For instance, let's say that we want to add a specific behavior that just allow us to add notes that contains the word Django in the title. Let's go back to the forms. What we need to do here is add a new method called `clean_title`. The field we want to add a validation, in this case, title. So in here we can get the title from the cleaned_data, which is a dictionary. The cleaned_data is returned by the form and is particularly useful for fields with strong validation. Like for instance, emails. In this scenario, it will be exactly the same value as the user passed. With this, we can actually start our validation. So if 'Django' not in title: we're going to raise a ValidationError with a message, 'We only accept notes about Django!' If everything goes well, we just return title.
```py
from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')
        
        return title

```
Django already injects the validation errors directly to our HTML. But we can't really control the design, so let's change this a little bit so we have a really good ValidationError here. We can go back, and on our `style.css`, we can add here that the `ul.errorlist` is not going to be displayed.
```css
ul.errorlist{
    display:none;
}
```
Then on the form template, we're going to add an if block. So if our form have errors, we're going to do something. So let's close the if, so we don't forget this, so endif. Then in here we're going to add a div, which is a class of type alert, and let's make it an alert-danger. Some vertical spacing. And in here, what we can do is pass the form.errors.title.as_text. Okay, let's go back, let's refresh this. And if I add a new note, which is a test, try to submit this. And there you go. Now you can add validations in any field you want with just a couple of additional methods in a form class.
```html
{% extends 'base.html'%} {%block content%}
<form action="{url 'notes.new'}" method="POST">
  {% csrf_token %} {{ form }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% if form.errors %}
    <div class="alert alert-danger my-5">
        {{form.errors.title.as_text}}
    </div>
{% endif%}

{% endblock %}

```

## Django forms are useful for layout as well
This form we just created, it's starting to look nice, but there's work to do here. It's still missing some style. An alternative would be to build the whole form by hand with each label and each input, everything. As you can see, this is not such a fun activity once you have a form already laid out for you, right? Forms are amazing because not only they add validation, but also because you can quickly add styles to it. First, let's say that we want to change the labels of our form. Title and text are the words we use on the backend, but that doesn't mean that it looks so good for our users. What we can do is on the class Meta, add a field called labels. And in here, let's add text. It's going to be, "Write your thoughts here." Let's save this. 

```py
from django.core.exceptions import ValidationError
from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels={
            'text':'Write your thoughts here',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')

        return title

```

Now, if we go back, and refresh this, as you can see, we are controlling the UX directly from our backend. We can also add an attribute widget to inject CSS classes directly to the form. Let's go back and add a new field called widgets. And then, in here, let's add title, and this is going to be a forms.TextInput. And then we're going to pass attributes. This is going to be a dictionary, and the class is going to be form-control and some vertical spacing, as usual. We can do a similar thing with the text. So text, this on the other hand, is not a TextInput, but a TextArea. And also we're going to add, again, attributes. And let's add the same classes. The class is equal to form-control and this. 

```py
from django.core.exceptions import ValidationError
from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text':forms.Textarea(attrs={'class': 'form-control mb-5'}),
        }
        labels={
            'text':'Write your thoughts here',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')

        return title

```

Let's go back and check it out. Refresh. Yeah. You can see now that controlling the frontend in an easy and accessible way is also a main advantage of using model forms. All this without ever changing the original template. Nice and easy.

## Codespaces error and the solution
