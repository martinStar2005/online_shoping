# Generated by Django 4.2.11 on 2024-04-15 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image_alter_comment_stars_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
