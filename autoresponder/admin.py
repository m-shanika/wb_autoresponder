from django.contrib import admin
from .models import Question, AnswerTemplate, Organization

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'created_date', 'answer_date')
    search_fields = ('question_id', 'text')
    readonly_fields = ('question_id', 'text', 'created_date', 'answer_text', 'answer_date')

@admin.register(AnswerTemplate)
class AnswerTemplateAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    search_fields = ('category_id', 'category_name')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'official_token')
    search_fields = ('name',)
