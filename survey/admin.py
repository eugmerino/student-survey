from django.contrib import admin
from .models import (
    Survey,
    ResponseGroup,
    Question,
    Option,
    Campaign,
    Assignment,
    Response
)


class QuestionInline(admin.TabularInline):
    model = Question
    list_filter = ('survey', 'response_group')
    search_fields = ('question',)
    autocomplete_fields = ('survey', 'response_group')
    extra = 1  # Número de preguntas vacías para agregar

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'objective')
    inlines = [QuestionInline]


@admin.register(ResponseGroup)
class ResponseGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_filter = ('response_group',)
    search_fields = ('text',)
    autocomplete_fields = ('response_group',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ('campaign', 'user', 'students')
    search_fields = ('campaign__name', 'user__username', 'student__name')


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    search_fields=('student_id',)