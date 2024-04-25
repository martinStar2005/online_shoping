from django.shortcuts import render
from orders.models import Order
from django.shortcuts import get_object_or_404, reverse, redirect
import requests
import json
from django.http import HttpResponse


def payment_process(request):
    # get the order
    order_id = request.session.get('user_order')
    order = get_object_or_404(Order, id=order_id)

    total_price_toman = order.total_price()
    total_price_rial = total_price_toman * 10

    zarinpal_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json'

    request_header = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    request_data = {
        'MerchantID': '123456123456123456123456123456123456',
        'Amount': total_price_rial,
        'Description': f'{order.id}: {order.first_name} {order.last_name}',
        'CallbackURL': request.build_absolute_uri(reverse('payment_callback')),
    }

    res = requests.post(
        url=zarinpal_url,
        data=json.dumps(request_data),
        headers=request_header,
    )

    data = res.json()
    authority = data['Authority']
    order.authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect(f'https://sandbox.zarinpal.com/pg/StartPay/{authority}')
    else:
        return HttpResponse('Error from zarinpal')


def payment_callback(request):
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')
    order = get_object_or_404(Order, authority=authority)

    total_price_toman = order.total_price()
    total_price_rial = total_price_toman * 10
    if status == 'OK':
        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }

        request_data = {
            "MerchantID": '123456123456123456123456123456123456',
            'Amount': total_price_rial,
            'Authority': authority,
        }
        res = requests.post(
            url='https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json',
            data=json.dumps(request_data),
            headers=request_header,
        )
        print(res)

        if 'errors' not in res.json():
            data = res.json()
            code = data['Status']

            if code == 100:
                order.is_paid = True
                order.save()

                return HttpResponse('تراکنش موفق...')

            elif code == 101:
                return HttpResponse('تراکنش موفق..')

    else:
        return HttpResponse('تراکنش ناموفق...')
