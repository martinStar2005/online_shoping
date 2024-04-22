from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(_('First name?'), max_length=30)
    last_name = models.CharField(_('last name?'), max_length=30)
    mobile_number = models.CharField(_('mobile number?'), max_length=15)

    address = models.CharField(_('address?'), max_length=300)
    description = models.CharField(_('any description?'), max_length=700, blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.is_paid}'

    def total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='products')

    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.order}'
