# Generated by Django 3.2 on 2021-04-21 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_products_serial_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
