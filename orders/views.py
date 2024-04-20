from django.shortcuts import render
from .forms import OrderForm


def create_order(request):
    context = {
        'form': OrderForm()
    }
    return render(request, 'orders/order_list.html', context)
