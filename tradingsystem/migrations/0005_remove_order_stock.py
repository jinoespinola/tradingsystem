# Generated by Django 3.2.8 on 2021-10-26 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradingsystem', '0004_order_stocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='stock',
        ),
    ]
