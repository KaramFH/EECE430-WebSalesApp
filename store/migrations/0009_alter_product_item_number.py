# Generated by Django 3.2 on 2021-05-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210505_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_number',
            field=models.CharField(max_length=255),
        ),
    ]
