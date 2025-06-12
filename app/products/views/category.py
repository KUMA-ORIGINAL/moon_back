from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from products.models import Category
from products.serializers import CategorySerializer


@extend_schema(tags=['Category'])
class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
