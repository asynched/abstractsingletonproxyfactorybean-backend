from django.contrib import admin
from core.models import Teacher, Task, Class, Notice, Resource, Lesson


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'imageUrl', 'email', 'about']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'attachments',
        'dueDate',
        'teacher',
    ]


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'teacher',
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'cls',
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
        'cls',
        'url',
    ]
