from django.contrib import admin
from core.models import Resource, Teacher, Task, Subject, Notice, Lesson


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'about',
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'dueDate',
        'teacher',
    ]


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'teacher',
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'subject',
        'schedule',
        'weekDay',
    ]


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
    ]
