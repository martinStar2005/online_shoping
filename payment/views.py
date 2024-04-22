from django.shortcuts import render
from orders.models import Order
from django.shortcuts import get_object_or_404


def payment_process(request):
    # get the order
    order_id = request.session.get('user_order')
    order = get_object_or_404(Order, id=order_id)

    total_price_toman = order.total_price()
    total_price_rial = total_price_toman * 10
