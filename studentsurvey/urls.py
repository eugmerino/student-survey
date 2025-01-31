from django.contrib import admin
from django.urls import path
from django.shortcuts import render  # Importamos render para la vista del home

# Definir la vista del home directamente en urls.py (opcional)
def home_view(request):
    return render(request, "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Nueva URL para el home
]
