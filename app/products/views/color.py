from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from products.models import Color
from products.serializers import ColorSerializer


@extend_schema(tags=['Color'])
class ColorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

