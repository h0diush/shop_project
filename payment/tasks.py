import os
from io import BytesIO

import weasyprint
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from orders.models import Order


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'BIG SHOP - Invoice no. {order_id}'
    message = 'Please, find attached the invoice for your recent purchase'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    html = render_to_string('orders/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [
        weasyprint.CSS(os.path.join(settings.STATIC_ROOT, 'pdf.css'))]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'order_{order_id}.pdf', out.getvalue(), 'application/pdf')
    email.send()
