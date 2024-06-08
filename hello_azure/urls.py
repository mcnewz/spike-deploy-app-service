from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('helloworld', views.hello_world, name='hello world'),
]