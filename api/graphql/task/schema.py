import graphene
import datetime as dt
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
        return Task.objects.filter(dueDate__gte=dt.datetime.utcnow()).order_by(
            'dueDate'
        )

    @login_required
    def resolve_task(root, info, uuid: str):
        return Task.objects.get(id=uuid)
