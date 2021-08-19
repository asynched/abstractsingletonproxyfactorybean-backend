import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from core.models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'


class TaskQueries(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)
    task = graphene.Field(TaskType, uuid=graphene.UUID(required=True))

    @login_required
    def resolve_all_tasks(root, info):
        return Task.objects.all()

    @login_required
    def resolve_task(root, info, uuid: str):
        return Task.objects.get(id=uuid)
