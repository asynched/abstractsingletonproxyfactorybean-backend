import graphene
from .types import TeacherType, TaskType
from core.models import Teacher, Task


class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)
    all_teachers = graphene.List(TeacherType)
    teacher = graphene.Field(TeacherType, uuid=graphene.String(required=True))

    def resolve_all_tasks(root, info):
        return Task.objects.all()

    def resolve_all_teachers(root, info):
        return Teacher.objects.all()

    def resolve_teacher(root, info, uuid: str):
        return Teacher.objects.get(id=uuid)


schema = graphene.Schema(query=Query)
