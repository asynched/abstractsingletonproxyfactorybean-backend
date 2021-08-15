from graphene_django import DjangoObjectType

from core.models import Task, Teacher


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__"


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = "__all__"
