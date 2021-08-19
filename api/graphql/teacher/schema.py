import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from core.models import Teacher


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherQueries(graphene.ObjectType):
    all_teachers = graphene.List(TeacherType)
    teacher = graphene.Field(TeacherType, uuid=graphene.UUID(required=True))

    @login_required
    def resolve_all_teachers(root, info):
        return Teacher.objects.all()

    @login_required
    def resolve_teacher(root, info, uuid: str):
        return Teacher.objects.get(id=uuid)
