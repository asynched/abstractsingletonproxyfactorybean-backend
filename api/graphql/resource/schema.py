import graphene
from graphene_django import DjangoObjectType
from core.models import Resource


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
        fields = "__all__"


class ResourceQueries(graphene.ObjectType):
    all_resources = graphene.List(ResourceType)

    def resolve_all_resources(root, info):
        return Resource.objects.all()
