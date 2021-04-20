# Generated by Django 3.2 on 2021-04-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('dateofbirth', models.DateField()),
                ('phonenumber', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('province', models.TextField()),
                ('city', models.TextField()),
                ('addresss', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
                ('item_number', models.TextField()),
                ('barcode', models.TextField()),
                ('serial_number', models.IntegerField()),
            ],
        ),
    ]
