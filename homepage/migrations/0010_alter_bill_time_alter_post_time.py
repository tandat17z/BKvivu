# Generated by Django 4.2.4 on 2023-11-27 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_alter_bill_sharer_alter_bill_time_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 22, 41, 36, 267177)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 22, 41, 36, 268150)),
        ),
    ]