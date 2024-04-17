from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/images', blank=True, verbose_name=_("Product's Image"))

    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


class Comment(models.Model):
    STARS_CHOICE = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'Normal'),
        ('4', 'good'),
        ('5', 'very good')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name=_('comment text!'))
    stars = models.CharField(max_length=1, choices=STARS_CHOICE, verbose_name=_('your score!'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('detail', args=[self.product_id])