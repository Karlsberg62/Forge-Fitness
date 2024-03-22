# Generated by Django 4.2.11 on 2024-03-22 18:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forgefitnessweb', '0004_alter_profile_address_alter_profile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Profile Picture'),
        ),
    ]
