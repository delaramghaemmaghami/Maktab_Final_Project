# Generated by Django 3.2.9 on 2021-12-27 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20211227_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='food_restaurant_category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.foodrestaurantcategory'),
        ),
    ]
