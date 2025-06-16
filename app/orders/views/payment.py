import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema

from config import settings
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


@extend_schema(tags=['Payment'])
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        order_id = session.metadata.get('order_id')

        if order_id:
            order = Order.objects.get(id=order_id)
            order.status = Order.Status.PAID
            order.save()

    return HttpResponse(status=200)
