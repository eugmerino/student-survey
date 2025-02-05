from django.contrib import admin
from django.urls import path, include  

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.custom_login, name='login'),
    path('survey/', include('survey.urls')),
]
