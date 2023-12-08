# Generated by Django 4.2.4 on 2023-12-08 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_alter_bill_time_alter_post_time_alter_product_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='avgStar',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 9, 56, 25, 588109)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 9, 56, 25, 588109)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 9, 56, 25, 588109)),
        ),
    ]
