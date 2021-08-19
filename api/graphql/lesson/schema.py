import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from core.models import Lesson


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonQueries(graphene.ObjectType):
    all_lessons = graphene.List(LessonType)
    lesson = graphene.Field(LessonType, uuid=graphene.UUID(required=True))
    lesson_by_day = graphene.List(LessonType, day=graphene.String(required=True))

    @login_required
    def resolve_all_lessons(root, info):
        return Lesson.objects.all()

    def resolve_lesson(root, info, uuid: str):
        return Lesson.objects.get(id=uuid)

    @login_required
    def resolve_lesson_by_day(root, info, day: str):
        return Lesson.objects.filter(weekDay=day)
