import graphene
import graphql_jwt

from api.graphql.task.schema import TaskQueries
from api.graphql.lesson.schema import LessonQueries
from api.graphql.teacher.schema import TeacherQueries
from api.graphql.subject.schema import SubjectQueries
from api.graphql.notice.schema import NoticeQueries
from api.graphql.user.schema import RegisterMutation, UserQueries
from api.graphql.resource.schema import ResourceQueries
from api.graphql.status.schema import StatusQueries


class Query(
    LessonQueries,
    TaskQueries,
    TeacherQueries,
    SubjectQueries,
    NoticeQueries,
    UserQueries,
    ResourceQueries,
    StatusQueries,
):
    pass


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register = RegisterMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
