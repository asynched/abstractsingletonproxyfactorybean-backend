import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from core.models import Notice


class NoticeType(DjangoObjectType):
    class Meta:
        model = Notice
        fields = '__all__'


class NoticeQueries(graphene.ObjectType):
    all_notices = graphene.List(NoticeType)
    notice = graphene.Field(NoticeType, uuid=graphene.UUID(required=True))

    @login_required
    def resolve_all_notices(root, info):
        return Notice.objects.all()

    @login_required
    def resolve_notice(root, info, uuid: str):
        return Notice.objects.get(id=uuid)
