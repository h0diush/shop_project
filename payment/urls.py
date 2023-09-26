from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'payment'

urlpatterns = [
    path('payment_process/', csrf_exempt(views.PaymentProcessView.as_view()),
         name='process'),
]
