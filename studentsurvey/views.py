from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#models
from survey.models import Assignment


@login_required(login_url='login')  # Redirige al login si no está autenticado
def home_view(request):
    user = request.user  # Obtiene el usuario autenticado
    assignments = Assignment.objects.filter(user=user)  # Filtra asignaciones del usuario
    students = set(student for assignment in assignments for student in assignment.students.all())  # Obtiene los estudiantes únicos

    return render(request, "home.html", {"students": students})


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