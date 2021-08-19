import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from core.models import Subject


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectQueries(graphene.ObjectType):
    all_subjects = graphene.List(SubjectType)
    subject = graphene.Field(SubjectType, uuid=graphene.UUID(required=True))

    @login_required
    def resolve_all_subjects(root, info):
        return Subject.objects.all()

    @login_required
    def resolve_subject(root, info, uuid: str):
        return Subject.objects.get(id=uuid)
