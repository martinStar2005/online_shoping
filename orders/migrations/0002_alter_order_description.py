# Generated by Django 4.2.11 on 2024-04-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=700, verbose_name='any description?'),
        ),
    ]
