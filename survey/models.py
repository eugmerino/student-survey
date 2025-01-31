from django.db import models
from django.contrib.auth.models import User
from student.models import Student

class Survey(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre de la encuesta"
    )
    objective = models.TextField(
        verbose_name="Objetivo de la encuesta"
    )

    def __str__(self):
        return self.name


class ResponseGroup(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre de conjunto de respuestas"
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(
        verbose_name="Pregunta"
    )
    survey = models.ForeignKey(
        Survey, 
        related_name='questions', 
        on_delete=models.CASCADE, 
        verbose_name="Encuesta"
    )
    response_group = models.ForeignKey(
        ResponseGroup, 
        related_name='questions', 
        on_delete=models.CASCADE, 
        verbose_name="Conjunto de respuestas"
    )

    def __str__(self):
        return self.question


class Option(models.Model):
    text = models.CharField(
        max_length=200, 
        verbose_name="Texto de la opción"
    )
    response_group = models.ForeignKey(
        ResponseGroup, 
        related_name='options', 
        on_delete=models.CASCADE, 
        verbose_name="Conjunto"
    )

    def __str__(self):
        return self.text


class Campaign(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre de campaña"
    )
    description = models.TextField(
        verbose_name="Descripción"
    )
    start_date = models.DateTimeField(
        verbose_name="Fecha de inicio"
    )
    end_date = models.DateTimeField(
        verbose_name="Fecha de finalización"
    )
    survey = models.ForeignKey(
        Survey, 
        related_name='Campaigns', 
        on_delete=models.CASCADE, 
        verbose_name="Encuesta"
    )

    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    campaign = models.ForeignKey(
        Campaign, 
        related_name='assignments', 
        on_delete=models.CASCADE, 
        verbose_name="Campaña"
    )
    user = models.ForeignKey(
        User, 
        related_name='assignments', 
        on_delete=models.CASCADE, 
        verbose_name="Maestro"
    )
    students = models.ManyToManyField(
        Student, 
        related_name='assignments', 
        verbose_name="Estudiantes"
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.campaign)