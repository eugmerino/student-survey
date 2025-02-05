from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Survey, Student, Option


@login_required(login_url='login')
def survey_detail(request, survey_id, student_id):
    survey = get_object_or_404(Survey, id=survey_id)
    student = get_object_or_404(Student, id=student_id)
    questions = survey.questions.all()

    questions_with_options = []
    for question in questions:
        options = Option.objects.filter(response_group=question.response_group)
        questions_with_options.append({"question": question, "options": options})

    if request.method == "POST":
        responses = {}
        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}")
            responses[question.id] = selected_option_id

        # Aquí puedes guardar las respuestas en la base de datos si lo deseas.
        return HttpResponse("Respuestas enviadas correctamente.")

    return render(
        request,
        "survey/survey_detail.html",
        {
            "survey": survey,
            "student": student,
            "questions_with_options": questions_with_options
        }
    )