from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from . import webhooks

app_name = 'payment'

urlpatterns = [
    path('payment_process/', csrf_exempt(views.PaymentProcessView.as_view()),
         name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('webhook/', csrf_exempt(webhooks.stripe_webhook),
         name='process'),
]
