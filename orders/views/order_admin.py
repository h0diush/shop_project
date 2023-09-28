from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render

from orders.models import Order


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/admin_detail.html", {'order': order})
