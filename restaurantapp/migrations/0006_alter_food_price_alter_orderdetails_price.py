# Generated by Django 4.2.7 on 2023-11-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0005_alter_food_price_alter_orderdetails_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
