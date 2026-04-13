

1. To start the Virtual Enviroment execute the following command: 
```bash
    ./venv/Scripts/activate
```

2. Install django with the following command
```bash
    pip install django
```

3.Create Django Project with the following command:
```bash
    django-admin startproject kanban .
``` 

4. Ensure that everything starting the server
```bash
   py manage.py runserver
```

5. Create Django App with command:
```bash
    py manage.py startapp board
```

6. Install application in the setting folder from the project kanban. 
```py
   INSTALLED_APPS =[
    ...
    #apps
    'board',
   ]
```

7. Create the first view of the app. Go the boar folder and open the view file.
```py
    from django.shortcuts import render
    from django.http import HttpResponse

    def board(request):
        return HttpResponse('Hello, wolrd')
```

8. Then go back to the ulrs file from the main project and update the file with:
```py
from django.urls import path

from board import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('home/',views.board),
]
```

9. Then we need to confirm that everything is working with the command
```py
   py manage.py runserver
```



## Minimum Working Page
Here we gone a explain how to return HTML page by using  the Django template languaje. 

1. Create a folder called `templates` inside of ur app folder. 
2. Inside this folder, we alsoe create another foler with the same name as our app. 
3. Inside this dolder, create a file call `board.html`
4. Now open the `views.py` file and change our base function. Insted of using `HttpResponse` we use the function render from `django.shortcuts`
```py
   from django.shorcuts import render
   from django.http import HttpResponse

   def board(request):
        #Render Functionw will need: original reuqest, the name of html template and empty brakets              
        return render(request, 'board/board.html',{})
```
5. We can use the brackets at the enf of the function as a way of passing down information from the view template. Lets pass today's date into dictionary with a key called today:
```py
    from django.shorcuts import render
    from django.http import HttpResponse
    from datetime import datetime

   def board(request):
        #Render Functionw will need: original reuqest, the name of html template and empty brakets              
        return render(request, 'board/board.html',{'today':datetime.today()})
```

6. The parameter will be pass to the HTML with the a double braktes: 
```html
<body>
    <h1>Welcome to SmartNotes</h1>
    <p>Today is {{today}}</p>
   </body>
```

When we created our first endpoint, we had to import `views.py` file from board into the the `urls.py` file from kanban
```py
    from django.contrib import admin
    from django.urls import include, path

    from board import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include("board.urls")),
    ]
```
This created a dependcy that wouldn't allow us to qucickly delete the board app. To do the things more organized we need to create another `urls.py` file inside the board app.  Here we need to create a very similar file that the one that we have in the board folder.

```py
  from . import views

  urlpatterns = [
    path('home', views.board),
  ]
```
In the project folder remove the dependencies that we implement and import the *include* funciton to pass the file as a string:
```py
   from django.contrib import admin
    from django.urls import include, path

    from board import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include("board.urls")),
    ]
```
With this configuration we remove the depencies between folder and now we have and stadalone aplication.


## Creating your First Django Project (Summary)

1. Start your Project
2. Create your first view
3. Use Teplates.
4. Apps and modularization
