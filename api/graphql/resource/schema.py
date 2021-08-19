import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from core.models import Resource


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
        fields = '__all__'


class ResourceQueries(graphene.ObjectType):
    all_resources = graphene.List(ResourceType)
    resource = graphene.Field(ResourceType, uuid=graphene.UUID(required=True))

    @login_required
    def resolve_all_resources(root, info):
        return Resource.objects.all()

    @login_required
    def resolve_resource(root, info, uuid: str):
        return Resource.objects.get(id=uuid)
