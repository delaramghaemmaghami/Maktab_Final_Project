# Generated by Django 3.2.9 on 2022-01-05 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0020_auto_20220105_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuorder',
            name='price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]