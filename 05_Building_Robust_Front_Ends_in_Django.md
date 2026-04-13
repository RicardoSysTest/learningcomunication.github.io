## Robus Front End with Django

## Static Files in Django
It is time to think about our project's front end. Our templates are too simple with just HTML on them, so let's add some colors! The first thing we need to do is create a folder where we're going to store all the static files, such as the CSS and JavaScript files, images, videos, et cetera. So let's go here, and create new folder `static`. Now we need to tell Django that this is the folder it needs to look into when searching for static files. To do that, let's go to the `smartnotes\settings.py`. Then in here, we can scroll down a little bit, and we're going to see here that there is a static URL already. 
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
Now we're also going to add static files, underline, dirs. This should be a list. And in here we're going to say, base dir, slash, static, which will lead Django to the folder we just created. 
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

Okay, now we can go back to the static, and create a new folder just for the CSS files, and one CSS file, let's call it style `static/css/style.css` . Okay, so in here we can create a simple CSS file. 

Let's create a class called, note-li, color equals red.   
```css
.note-li{
    color: red;
}
```
What we need to do now is make sure that our template, and Django per se, recognizes this file. So let's go to the notes, and let's try the `notes_list.html`. The first thing we need to do is actually tell Django that this HTML is going to use the static files. So let's go curly brackets, percentages, and load static (`{% load static %}`). Okay, now what we need here is to add a CSS file as we would in any HTML file. So let's create a head, then a link. So the rel is going to be stylesheet. The type is going to be text, CSS, and on the href, we're going to use the Django template language to add our URL. So let's call static, then CSS style dot CSS. That's it. That's all we need to do to have the CSS being rendered on this file. So let's go here to tag `li`, and add the class, which is going to be our class name `<li class="note-li"></li>`, let's save it and try it.
```html
{% load static %}
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css'%}"/>
  </head>
  <h1>These are the notes</h1>
  <ul>
    {% for note in notes %}
    <li class="note-li">{{note.title}}</li>
    {% endfor %}
  </ul>
</html>

```
I'm going to refresh this. And there you go. Now the notes are red because the CSS is being rendered and used in this file. If we open the inspector here, we can see here that the head is appearing. We have the href here being correctly rendered, and then each note here has the class that has the attribute of color red. If you hover this href, you'll notice that this is actually a link. So let's go here. Let's copy this, and then we can replace it here. And there you go. As you can see here, this is the file we just created. So actually, Django is locating the file, and loading it automatically into the templates. There you go. Now you can use CSS in all your templates.


## An HTML Skeleton: How to set up a base structure to every Django template
As we've seen, it's pretty easy to add CSS files into Django template, but it would be quite exhaustive to need to always remember to add the CSS link to all templates we have in all our apps. If you're thinking that there must be a better way of doing this, you're absolutely right. What we need now is a base template. Let's create a base template `templates/base.html`. Here, we can load static on the top of the file and  create a  HTML body: 
```html
{% load static %}
<html>
  <head>
     <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}" />
  </head>
  <body>
    {% block content%}
    {% endblock %}
  </body>
</html>
```
In the body of the HTML we add the command `{% block content%}`, you can call this content, whatever you like. The important thing here is to know that this is a block area where we can inject things. Let's go back to the notes and open the notes list template. So in here, what we can do is extends `base.html` and  get rid of all this basic HTML stuff here and use this block content here
```html
{% extends 'base.html' %}

{% block content %}
  <h1>These are the notes</h1>
  <ul>
    {% for note in notes %}
    <li class="note-li">{{note.title}}</li>
    {% endfor %}
  </ul>
{% endblock %}
```
What we're doing here, we're taking only the important part of our template and wrapping it on the block content command so this can be injected on the base template. 

Let's try it out. Okay, so we have a problem here. The template is showing as non-existent. So you can see here where Django was trying to search for a base HTML template. So you can see that it tried in multiple places, including the two templates folder in home and notes app, but as you can see, the static folder templates is not being looked for. So what we need to do is tell Django where to look for. Let's go to settings file, and down below, we're going to find out that there is a templates, and there is a list of directories that we can add here. So similar to what we did on the static files, we're going to add that particular folder in here. 
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'static/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
 What's happening here is that with this syntax, we can define the basics of our HTML in our base.html template, and then we create each webpage as a separate template that extends the base. So we will build each template separately and just the small parts, but we'll then inject it to the base template where we can have all our default configurations, such as the CSS files and the JavaScripts. This will allow us to keep each webpage template as simple as we can while keeping all the configuration in a single place. That's another power of the Django template language. Now that you know exactly how to use a base template, I encourage you to go back and try it out in all the templates we have so far.

* If yo Need a Template please review Bulma [Framework](https://bulmatemplates.github.io/bulma-templates/templates/kanban.html)

## Its time to Add some style
Okay so instead of defining all of the CSS, we want to speed up our front end a little bit. So let's use a CSS framework. We're going to use bootstrap for now. So what we need to do is on the static, `base.html`, I'm going to change this CSS we just created with the link to the bootstrap framework version five. So we can go back, delete this line and that's it. 
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    />
    <title>Smart Notes</title>
  </head>
  <body>
      {% block content%} {% endblock %}
  </body>
</html>
```
So the first thing we can do here is on top of the block content, let's add a div. And then on this div, let's add a class equals to my five, text center and container. 
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    />
    <title>Smart Notes</title>
  </head>
  <body>
    <div class="my-5 text-center container">
      {% block content%} {% endblock %}
    </div>
  </body>
</html>
```
Okay, so now we can go to the home page and check the changes that the bootstraps already made. So let's go here. You can see here now that the style's a little bit better. We have more spacing, the text is in center, et cetera. 

So let's add a button on the homepage that will lead us to the list of notes. So let's go to home. Here, we can add anchor type with href. Let's leave it empty for now. 
```html
{% extends "base.html"%} {% block content %}
<h1>Welcome to Smartnotes !</h1>
<p>Today is {{today}}</p>
<a href="" class="btn btn-primary">Check out these smart notes!</a>
{% endblock %}
```

Then in here, we're going to use two classes, BTN for button and BTN primary for the style. Then check out these smart notes. Okay, so if we go back, we can see now that we have a button, but it doesn't do anything. So how do we deal with links here? We could hard code the link to our local host, but imagine that when we deploy our website, we need to remember to come back and change everything. Not so good. Thankfully, the Django template language has a function for that. What we need to do is the following. Let's open curly brackets and percentage and then use URL. And then in here, we're going to say notes.list. 
```html
{% extends "base.html"%} {% block content %}
<h1>Welcome to Smartnotes !</h1>
<p>Today is {{today}}</p>
<a href="{% url 'notes.list'%}" class="btn btn-primary">Check out these smart notes!</a>
{% endblock %}
```

Okay you might be wondering, okay, how Django knows which endpoint to link. It doesn't, and we need to tell it. So let's go back to notes URLs. And in here, what we're going to do is add a name. So we can give a name, notes.list. That's all we need for Django to define each endpoint we are pointing to, no matter if you're on local host or production. Let's test it out. Let's click here, and there you go.
```py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetailView.as_view()),
]
```
 We're being redirected to this template that also needs some styling. We'll get there. So let's go back to this page and try to style it up a little bit. So let's go to notes list. And in here, we need a couple of things. So first, we can add some vertical styling here. So we're going to use my five here, okay? And let's use a couple of divs here to have some cards. So bear with me just a little longer. So in here, instead of the UL, we're going to use a div, and this div's going to have class is equal row. Row cols3 and g-2, then we're going to have another div here, and this div is going to have a class equals to call. Okay, and finally we're going to have another div that is going to have a class=p-3 border. Okay. So this here is going to be a row, and we're going to have each card to be a column. So what we can do here now is say that for note in notes, we're going to have in here, let's add a title. So it's going to have here, note.title, and then let's end the four here. And let's leave it for now like this so we can remove this.
 ```html
 {% extends 'base.html' %} {% block content %}
<h1 class="my-5">These are the notes:</h1>
<div class="row row-cols3 g-2">
  {% for note in notes %}
  <div class="col">
    <div class="p-3 border">
      <h3>{{note.title}}</h3>
    </div>
  </div>
  {% endfor %}
</div>

{% endblock %}
 ```
 
 This would look a little bit better if we could display some of the text of a note, but not all of it. We can use the truncate charts function to do this. Let's try it out. So in here, let's add note.text, and then with the pipe truncate chars, let's just leave it at 10. So this is going to display 10 characters. So let's try it out. And there you go. 
  ```html
 {% extends 'base.html' %} {% block content %}
<h1 class="my-5">These are the notes:</h1>
<div class="row row-cols3 g-2">
  {% for note in notes %}
  <div class="col">
    <div class="p-3 border">
      <h3>{{note.title}}</h3>
      {{note.text|truncatechars:10}}
    </div>
  </div>
  {% endfor %}
</div>

{% endblock %}
 ```
 So what's happening here is that Django is taking the text and just displaying the first 10 characters, plus the three dots. 
 
Okay, so it's still missing a couple of things, so we can't really access all the details of that particular note. So we're almost there. First, let's give a name to the detail URLs as well. So let's go back, url.py, and then in here, let's add name is equal to notes.detail. 
```py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
]

```
Okay, so now we can go back and in the title, we can add the link. So it's going to be an A with href is equal to the url, and then notes.detail. Let's pass this to here. It's still missing something. So we also need to pass here, the pk. So the pk is going to be the node.id. Pretty simple. We can also add some classes here just to make it a little bit prettier. So let's pass class is equals to text dark, and text decoration non. 
```html
{% extends 'base.html' %} {% block content %}
<h1 class="my-5">These are the notes:</h1>
<div class="row row-cols3 g-2">
  {% for note in notes %}
  <div class="col">
    <div class="p-3 border">
      <a
        href="{% url 'notes.detail' pk=note.id %}"
        class="text-dark text-decoration-non"
        ><h3>{{note.title}}</h3></a
      >
      {{note.text|truncatechars:10}}
    </div>
  </div>
  {% endfor %}
</div>

{% endblock %}

```

So let's go back, notes detail, and let's just add here, a div. This should be in here. And on this div, let's add a class border. Let's make it round, and just add some style on the H1. So my equals five. Okay, I think we're done here. Let's go back. Yeah, so all done. Now you have style and dynamically generated links.
```html
{% extends "base.html" %} {% block content %}
<div class="border round">
  <h1 class="my-5">{{note.title}}</h1>
  <p>{{note.text}}</p>
</div>
{% endblock %}
```
