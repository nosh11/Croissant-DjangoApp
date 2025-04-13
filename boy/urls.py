from django import urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from boy import views

from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
]