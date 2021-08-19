import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from django.contrib.auth.models import User
from api.graphql.types import (
    RegisterMutation,
    TeacherType,
    TaskType,
    ClassType,
    LessonType,
    NoticeType,
    ResourceType,
    UserType,
)
from core.models import Task, Teacher, Class, Lesson, Notice, Resource


class Query(graphene.ObjectType):
    """A list of all queries in the backend"""

    all_tasks = graphene.List(TaskType)
    all_teachers = graphene.List(TeacherType)
    all_classes = graphene.List(ClassType)
    all_lessons = graphene.List(LessonType)
    all_notices = graphene.List(NoticeType)
    all_resources = graphene.List(ResourceType)
    task = graphene.Field(TaskType, uuid=graphene.UUID(required=True))
    teacher = graphene.Field(TeacherType, uuid=graphene.UUID(required=True))
    clazz = graphene.Field(ClassType, uuid=graphene.UUID(required=True))
    lesson = graphene.Field(LessonType, uuid=graphene.UUID(required=True))
    notice = graphene.Field(NoticeType, uuid=graphene.UUID(required=True))
    resource = graphene.Field(ResourceType, uuid=graphene.UUID(required=True))
    user = graphene.Field(UserType)

    lesson_by_day = graphene.List(LessonType, day=graphene.String(required=True))

    @login_required
    def resolve_all_tasks(root, info):
        return Task.objects.all()

    @login_required
    def resolve_all_teachers(root, info):
        return Teacher.objects.all()

    @login_required
    def resolve_all_classes(root, info):
        return Class.objects.all()

    @login_required
    def resolve_all_lessons(root, info):
        print(info.context.user)
        return Lesson.objects.all()

    @login_required
    def resolve_all_notices(root, info):
        return Notice.objects.all()

    @login_required
    def resolve_all_resources(root, info):
        return Resource.objects.all()

    @login_required
    def resolve_teacher(root, info, uuid):
        return Teacher.objects.get(id=uuid)

    @login_required
    def resolve_clazz(root, info, uuid):
        return Class.objects.get(id=uuid)

    @login_required
    def resolve_lesson(root, info, uuid):
        return Lesson.objects.get(id=uuid)

    @login_required
    def resolve_notice(root, info, uuid):
        return Notice.objects.get(id=uuid)

    @login_required
    def resolve_resource(root, info, uuid):
        return Resource.objects.get(id=uuid)

    @login_required
    def resolve_lesson_by_day(root, info, day):
        return Lesson.objects.filter(weekDay=day)

    @login_required
    def resolve_user(root, info):
        return info.context.user


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register = RegisterMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
