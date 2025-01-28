from django.contrib import admin
from .models import Survey, ResponseGroup, Question, Option, Campaign, Assignment


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'objective')


@admin.register(ResponseGroup)
class ResponseGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'survey', 'response_group')
    list_filter = ('survey', 'response_group')
    search_fields = ('question',)
    autocomplete_fields = ('survey', 'response_group')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'response_group')
    list_filter = ('response_group',)
    search_fields = ('text',)
    autocomplete_fields = ('response_group',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'survey')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'user', 'student')
    list_filter = ('campaign', 'user', 'student')
    search_fields = ('campaign__name', 'user__username', 'student__name')