# Generated by Django 4.2.11 on 2024-04-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authority',
            field=models.CharField(blank=True, max_length=700),
        ),
    ]
