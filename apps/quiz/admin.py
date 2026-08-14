from django.contrib import admin
from .models import Fairy, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


@admin.register(Fairy)
class FairyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "question", "fairy")