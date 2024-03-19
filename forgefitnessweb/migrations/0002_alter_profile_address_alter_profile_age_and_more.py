# Generated by Django 4.2.11 on 2024-03-19 22:27

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forgefitnessweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postcode',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='foggy-bg.jpg', max_length=255, verbose_name='Profile Picture'),
        ),
    ]
