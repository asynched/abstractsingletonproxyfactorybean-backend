from django.contrib import admin
from core.models import Attachment, Teacher, Task, Subject, Notice, Resource, Lesson


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


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'url',
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


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'subject',
        'url',
    ]
