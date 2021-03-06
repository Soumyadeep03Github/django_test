<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Django Test</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A Django Project having 2 models that can track user's activity.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Using this app we can add a new user and also add entries of their activities.

## 🏁 Getting Started <a name = "getting_started"></a>

Download the git repo in your local or clone it

### Prerequisites

Python > 3.5 (recommend) must be installed with pip package installer


### Installing

## Install using pipenv:
Open the cloned folder in terminal or command prompt for windows
### execute the folloing command to install all the dependencies of the project:
pipenv install --skip-lock
### Enable the virtual environment using the command:
pipenv shell
### Migrate the model changes:
python manage.py migrate
### Create a superuser if you want to check all the models in admin panel by executing the below command and providing login information(Optional)
python manage.py createsuperuser
### Run the Django app
python manage.py runserver

#### Install using pip(without virtual environment):
Open the cloned folder in terminal or command prompt for windows
### execute the folloing command to install all the dependencies of the project:
pip install -r requirement.txt
### Migrate the model changes:
python manage.py migrate
### Create a superuser if you want to check all the models in admin panel by executing the below command and providing login information(Optional)
python manage.py createsuperuser
### Run the Django app
python manage.py runserver

### Open the app in browser
Open the below link in any browser:
127.0.0.1:8000


## 🎈 Usage <a name="usage"></a>

The following APIs are available:
YOUR_WEB_URL/api => Show all the available data in json format
YOUR_WEB_URL/api/insert/ => insert a data into the database [id = new(for new entry)]


## 🚀 Deployment <a name = "deployment"></a>
### Create Account
Create an account in Heroku
### Install CLI
Install Heroku CLI and login to Heroku
### Create Procfile
create a procfile in the folder 
add web: gunicorn myproject.wsgi
### Install django-heroku
pipenv install django-heroku
### Add important lines to settings.py file
Add the following import statement to the top of settings.py:
import django_heroku
Then add the following to the bottom of settings.py:
#Activate Django-Heroku.
django_heroku.settings(locals())
### install gunicorn 
pipenv install gunicorn
### Heroku Create an app
heroku create "app-name"
### git push in heroku
git push heroku master
Open the website
if the website is not working then use heroku run bash
## ⛏️ Built Using <a name = "built_using"></a>

- [SQLITE](https://www.sqlite.org/) - Database
- [Django](https://www.djangoproject.com/) - Server Framework

## ✍️ Authors <a name = "authors"></a>

- [@Soumyadeep](https://github.com/Soumyadeep03Github/) 