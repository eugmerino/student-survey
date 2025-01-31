from django.contrib import admin
from django.urls import path
from django.shortcuts import render  # Importamos render para la vista del home
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.custom_login, name='login'),
]
