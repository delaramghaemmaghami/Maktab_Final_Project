# Generated by Django 3.2.9 on 2022-01-05 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_alter_menuorder_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
