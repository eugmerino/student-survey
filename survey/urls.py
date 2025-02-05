from django.urls import path
from .views import survey_detail

urlpatterns = [
    path("<int:survey_id>/<int:student_id>", survey_detail, name="survey_detail"),
]