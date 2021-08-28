import graphene
from graphene_django import DjangoObjectType
from core.models import Attachment


class AttachmentType(DjangoObjectType):
    class Meta:
        model = Attachment
        fields = "__all__"


class AttachmentQueries(graphene.ObjectType):
    all_attachments = graphene.List(AttachmentType)

    def resolve_all_attachments(root, info):
        return Attachment.objects.all()
