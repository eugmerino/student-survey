from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json
import datetime
from django.forms.models import model_to_dict

from .models import (
    Survey,
    Student,
    Option,
    Campaign,
    Response
)


def json_datetime_handler(obj):
    """Convierte objetos datetime a string ISO 8601."""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


@login_required(login_url='login')
def survey_detail(request, campaign_id, survey_id, student_id):

    survey = get_object_or_404(Survey, id=survey_id)
    student = get_object_or_404(Student, id=student_id)

    questions = survey.questions.all()

    questions_with_options = []
    for question in questions:
        options = Option.objects.filter(response_group=question.response_group)
        questions_with_options.append({
            "question": model_to_dict(question),
            "options": [model_to_dict(option) for option in options]
        })

    if request.method == "POST":
        campaign = get_object_or_404(Campaign, id=campaign_id)
        responses = {}
        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}")
            responses[question.id] = selected_option_id

        data = {
            "campaign": model_to_dict(campaign),
            "survey": model_to_dict(survey),
            "questions": questions_with_options,
            "responses": responses
        }

        # Crear la respuesta
        response_instance = Response.objects.create(
            student=student,
            response=json.dumps(data,default=json_datetime_handler, indent=2)
        )
        response_instance.save()
        # 

        return render(
            request,
            "survey/survey_detail.html",
            {
                "survey": survey,
                "student": student,
                "questions_with_options": questions_with_options,
                "completed": True
            }
        )

    return render(
        request,
        "survey/survey_detail.html",
        {
            "survey": survey,
            "student": student,
            "questions_with_options": questions_with_options,
            "completed": False,
        }
    )
