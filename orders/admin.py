from django.contrib import admin

from .models import OrderItem, Order

from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'quantity', 'price')
    extra = 0


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'datetime_created', 'is_paid')

    inlines = [
        OrderItemAdmin,
    ]
