from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('nextpage', views.nextpage,name='nextpage'),
    path('previouspage', views.previouspage,name='previouspage'),


]
