from django.urls import path
from .views import StudentCreateView, StudentUpdateView, StudentListView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list"),
    path("student/new/", StudentCreateView.as_view(), name="student_create"),
    path("student/edit/<int:pk>/", StudentUpdateView.as_view(), name="student_edit"),
]