# Generated by Django 3.2 on 2021-04-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='', upload_to='product_pictures'),
        ),
    ]
