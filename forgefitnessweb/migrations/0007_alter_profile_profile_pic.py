# Generated by Django 4.2.11 on 2024-03-22 19:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forgefitnessweb', '0006_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='ry0iwt4v2feszvwwxlra.png', max_length=255, verbose_name='Profile Picture'),
        ),
    ]
