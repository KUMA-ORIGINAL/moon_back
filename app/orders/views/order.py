from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, permissions

from ..models import Order
from ..serializers import OrderCreateSerializer


@extend_schema(tags=['Order'])
class OrderViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin):

    def get_serializer_class(self):
        return OrderCreateSerializer

    def get_queryset(self):
        return Order.objects.all()
