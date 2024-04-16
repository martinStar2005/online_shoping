from django.contrib import admin

from products.models import Product, Comment

from jalali_date.admin import ModelAdminJalaliMixin


class ProductComment(admin.TabularInline):
    model = Comment
    fields = ('author', 'product', 'stars', 'active')
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'active',)

    inlines = [
        ProductComment,

    ]
