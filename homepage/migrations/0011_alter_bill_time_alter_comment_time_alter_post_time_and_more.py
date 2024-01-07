# Generated by Django 4.2.7 on 2024-01-07 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_comment_time_alter_bill_time_alter_post_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 13, 0, 53, 480731)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 13, 0, 53, 482727)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 13, 0, 53, 481727)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 13, 0, 53, 480731)),
        ),
    ]
