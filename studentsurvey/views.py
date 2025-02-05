from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#models
from survey.models import Assignment


@login_required(login_url='login')
def home_view(request):
    user = request.user  
    assignments = Assignment.objects.filter(user=user).prefetch_related('students')  

    data = []
    for assignment in assignments:
        students_list = [
            {"id": student.id, "name": f"{student.name} {student.last_name}", "NIE": student.NIE}
            for student in assignment.students.all()
        ]
        data.append({
            "id": assignment.id,
            "campaign": assignment.campaign,
            "user": assignment.user,
            "students": students_list
        })

    return render(request, "home.html", {"assignments_data": data})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Formulario no válido.')
    else:
        form = AuthenticationForm()

    # Asignar las clases de bootstrap a los campos del formulario
    form.fields['username'].widget.attrs['class'] = 'form-control'
    form.fields['password'].widget.attrs['class'] = 'form-control'

    return render(request, 'login.html', {'form': form})