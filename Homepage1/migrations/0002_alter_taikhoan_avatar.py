# Generated by Django 4.2.7 on 2023-11-24 18:54

import Homepage1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taikhoan',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=Homepage1.models.image_upload_path),
        ),
    ]
