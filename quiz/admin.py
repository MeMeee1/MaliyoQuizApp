from django.contrib import admin
from quiz import models


@admin.register(models.Form)
class FormAdmin(admin.ModelAdmin):
    ...


@admin.register(models.FormQuestion)
class FormQuestionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    ...
