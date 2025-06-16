import stripe
from django.conf import settings
from rest_framework import serializers

from .order_item import OrderItemCreateSerializer
from ..models import Order, OrderItem


class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = OrderItemCreateSerializer(many=True, write_only=True)
    checkout_url = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_items',
            'first_name',
            'last_name',
            'company',
            'country',
            'street_address',
            'city',
            'state',
            'zip_code',
            'phone',
            'email',
            'order_notes',
            'checkout_url'
        ]
        extra_kwargs = {
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'company': {'write_only': True},
            'country': {'write_only': True},
            'street_address': {'write_only': True},
            'city': {'write_only': True},
            'state': {'write_only': True},
            'zip_code': {'write_only': True},
            'phone': {'write_only': True},
            'email': {'write_only': True},
            'order_notes': {'write_only': True},
        }

    def validate_order_items(self, value):
        if not value:
            raise serializers.ValidationError("Требуется добавить хотя бы один товар в заказ.")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        total_price = 0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )
            total_price += price

        order.total_price = round(total_price, 2)
        order.save()

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  # или 'rub' если нужна другая валюта
                        'product_data': {
                            'name': f'Order #{order.id}',
                        },
                        'unit_amount': int(order.total_price * 100),  # Цена в центах
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            metadata={
                "order_id": order.id
            },
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )

        self._context['checkout_url'] = checkout_session.url
        order.checkout_url = checkout_session.url
        return order

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['checkout_url'] = getattr(instance, 'checkout_url', self._context.get('checkout_url', ''))
        return data
