from rest_framework import serializers

from ..models import OrderItem


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity',]
