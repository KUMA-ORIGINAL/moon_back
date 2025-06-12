from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from products.models import Tag
from products.serializers import TagSerializer


@extend_schema(tags=['Tag'])
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
