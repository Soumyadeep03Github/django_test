from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/insert/', views.datainsertion),
    path('api', views.fetchData_api),
    path('', views.index, name='index'),
]