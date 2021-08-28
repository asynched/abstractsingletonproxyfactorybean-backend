import graphene
from core.models import Notice, Task, Resource
from graphql_jwt.decorators import login_required


class CourseStatus(graphene.ObjectType):
    tasks = graphene.Int()
    notices = graphene.Int()
    resources = graphene.Int()

    def resolve_tasks(root, info):
        return Task.objects.count()

    def resolve_notices(root, info):
        return Notice.objects.count()

    def resolve_resources(root, info):
        return Resource.objects.count()


class StatusQueries(graphene.ObjectType):
    course_status = graphene.Field(CourseStatus)

    @login_required
    def resolve_course_status(root, info):
        return CourseStatus()
