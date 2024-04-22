from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem


@login_required
def create_order(request):
    order_form = OrderForm()
    cart = Cart(request)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if len(cart) == 0:
            messages.warning(request, _('Your cart is empty and you can add product in your cart first...'))
            return redirect('product_list')

        if order_form.is_valid():
            form_obj = order_form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=form_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            cart.clear()

            request.user.first_name = form_obj.first_name
            request.user.last_name = form_obj.last_name
            request.user.save()

            request.session['user_order'] = form_obj.id
            return redirect('payment_process')


    return render(request, 'orders/order_list.html', {
        'form': order_form
    })
