from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _

from products.models import Product
from .cart import Cart
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['quantity_form'] = AddToCartForm(initial={
            'quanity': item['quantity'],
            'inplace': True
        })

    context = {
        'cart': cart
    }
    
    return render(request, 'cart/cart_detail.html', context )


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace=cleaned_data['inplace'])

    return redirect('product_list')


def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('product_list')


def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _('Cart cleared successfully'))

    else:
        messages.warning(request, _('Your cart is already cleared'))

    return redirect('cart:cart_detail')

