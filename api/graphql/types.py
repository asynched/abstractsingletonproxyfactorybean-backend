from graphene_django import DjangoObjectType

from core.models import Task, Teacher, Class, Lesson, Notice, Resource


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__"


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = "__all__"


class ClassType(DjangoObjectType):
    class Meta:
        model = Class
        fields = "__all__"


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson
        fields = "__all__"


class NoticeType(DjangoObjectType):
    class Meta:
        model = Notice
        fields = "__all__"


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
        fields = "__all__"
