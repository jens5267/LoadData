# Creating a new project with Django
To start a project in Django, it is recommended to use a virtualenv.

## Setup the project
Working steps:  
`mkdir <project name>` <!-- trydjango -->
`cd <project name>`  
`virtualenv -p python3 .`  
`source bin/activate`  
`pip install django==2.0.7`  
`mkdir src`  
`cd src`  
`django-admin startproject <project name> .` <!-- trydjango -->  
`cd <project name>`  
`python manage.py migrate` <!-- run every time the model is changed-->  
`python manage.py makemigrations`  
`python manage.py createsuperuser`  
`python manage.py startapp <app name>` <!-- products -->  
<!-- create model in <app name> -> models.py -->  
<!-- add <app name> to settings.py at INSTALLED_APPS -->  
`python manage.py makemigrations`  
`python manage.py migrate`  
<!-- register <model> at admin.py > -->  
create view in <app name> views.py


Most likely also working, not properly tested though
Create the project
`django-admin startproject <projectname>` 
<!-- trydjango -->

## Use virtualenv
Install virtualenv
`pip install virtualenv`
Create and activate a virtualenv
`virtualenv <virtualenv name>`
<!-- trydjango -->
`source <virtualenv name> bin/activate`
## Create a .gitignore
`touch .gitignore`
Use the .gitignore file on github

Create an admin user:
`python manage.py createsuperuser`
You have to put in a username and a password, an email is not mandatory.

Create the app
`django-admin startapp <appname>`
<!-- products -->


`python manage.py makemigrations`
`python manage.py migrate`


