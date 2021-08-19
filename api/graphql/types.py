import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth.models import User
from core.models import Task, Teacher, Class, Lesson, Notice, Resource


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class RegisterMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)

    username = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, password):
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.save()

        return RegisterMutation(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )


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
