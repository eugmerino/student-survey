# Generated by Django 4.2.18 on 2025-01-27 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0002_responsegroup_remove_option_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de campaña')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de finalización')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='survey.campaign', verbose_name='Campaña')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='student.student', verbose_name='Estudiante')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL, verbose_name='Maestro')),
            ],
        ),
    ]
