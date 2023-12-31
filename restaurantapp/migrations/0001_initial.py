# Generated by Django 4.2.7 on 2023-11-14 08:58

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=300, verbose_name='Gender')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('ID_Number', models.IntegerField()),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=300, verbose_name='Gender')),
                ('phoneNumber', models.CharField(max_length=50)),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.district')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderId', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('orderDate', models.DateField()),
                ('DeliveryTime', models.TimeField()),
                ('price', models.CharField(default='0', max_length=20)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.customer')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=50)),
                ('Items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.food')),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.orderdetails')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.state'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.state'),
        ),
    ]
