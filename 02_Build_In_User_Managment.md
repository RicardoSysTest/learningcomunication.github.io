
# 02 User Manager from Django Framwework

## Django Admin Easly Visualizing and Creating Data
By default django will have and entire authentication system ready to go. The only thing we need to do is to make sure our database is properly configure. Django knows if the database is behind the system changes trough a couple of files colled migrations. By default Django already has the migrations for the authtnetication system ready, so what you need to do is apply them to the database, so what you need to do is apply them to the database with the command migrate:
```bash
   py managege.py migrate
```

Since now out database is up to speed with Django, what we need is to create a superuser that will have all the power that it can in this Django project. We do this by running the command `createsuperuser`.

## Migrations: Making Database Changes Easy
Create user with the Django Addmin is a safe way to handle multiple users.


## User authentication in two simples steps
You learn that Django comes with a power authentication system already to be used. 

1. Come back to the templates folder and go to the sub-folder home. Here create a new file call `authorized.html`
```html
<html>
   <h1></h1>
</html>
```
2. Now we can go back to the `views`.py` file from our application folder and create a very similar function to home. But this time we're going to display the authorized template.
```py

def home(request):
   return render(request, 'board/index.html',{'today':datetime.today()})

def authorized(request):
   return  render(request, 'board/auuthorized.html',{})
```
3.  Let's import the login_required `django.contrib.auth.decorators` . And add this function as a decorator to our authorized function to block the access of this webpage if a user is not logged in. 
```py
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, 'board/index.html',{'today':datetime.today()})

@login_required
def authorized(request):
   return  render(request, 'board/authorized.html',{})
```

4. Then we need to update the `urls.py` from the application. Now we can go back and try to access the authorized endpoint. There you go, we can see the template we created. This is only possible because we're logged in via the Django admin interface. If we go back to the admin and log out. And try to re-access the authorized area, you see here that we get a 404, meaning that this page was not found. 
```py
 from django.urls import path
 from . import views

 urlpattern =[
   path('home', views.home),
   path('authorized',views.authorized)
 ]
```

5. We want the user to know that they need to be logged in to access this page and maybe 404 is not a really nice flow.  The ideal flow is that we redirect them to the login page. To do this, we need to go back to the views file and add a perimeter called login_url. 
```py
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, 'board/index.html',{'today':datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
   return  render(request, 'board/authorized.html',{})
```
And let's pass this as slash admin. If we go back and try to access it again. And there it is. Since we are not locked in, Django understand that it needs to redirect me to the login URL, which for now was defined as the admin endpoint. How amazingly simple was to add authentication to this endpoint