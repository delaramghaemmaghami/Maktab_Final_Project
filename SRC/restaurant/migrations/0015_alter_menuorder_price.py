# Generated by Django 3.2.9 on 2022-01-05 08:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_alter_menuorder_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuorder',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
