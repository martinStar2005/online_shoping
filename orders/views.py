from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


@login_required
def create_order(request):
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            form_obj = order_form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()

    return render(request, 'orders/order_list.html', {
        'form': order_form
    })
