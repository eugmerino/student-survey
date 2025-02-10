from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#models
from .models import Student
#funcions
from studentsurvey.commons import get_user_group


@login_required(login_url='login')
def person_list(request):
    # Verificar si el usuario pertenece al grupo "admin"
    if not request.user.groups.filter(name="admin").exists():
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')
    
    estudents = Student.objects.all().order_by('name') 
    paginator = Paginator(estudents, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'person/person_list.html', {
        'page_obj': page_obj,
        'menu': get_user_group(request.user)
    })


@login_required(login_url='login')
def person_update(request, person_id):
    print(person_id)
    return render(request, 'person/person_new.html', {
        'menu': get_user_group(request.user)
    })