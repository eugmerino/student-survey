from django.urls import path
from .views import person_list, person_update

urlpatterns = [
    path("list", person_list, name="person_list"),
    path("<int:person_id>", person_update, name="person_update"),
]