# Generated by Django 3.2 on 2021-05-05 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210502_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='picture',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
