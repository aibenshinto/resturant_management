# Generated by Django 4.2.7 on 2023-11-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_alter_orderdetails_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='price',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
