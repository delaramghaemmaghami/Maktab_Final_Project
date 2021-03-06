# Generated by Django 3.2.9 on 2021-12-26 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_main', models.BooleanField()),
                ('description', models.TextField(max_length=500)),
                ('food_restaurant_category', models.CharField(max_length=50)),
                ('restaurant', models.CharField(max_length=50)),
                ('branch_address', models.CharField(max_length=50)),
                ('manager', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BranchAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('meal_category', models.CharField(max_length=200)),
                ('food_restaurant_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FoodRestaurantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.PositiveIntegerField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('meal_category', models.CharField(max_length=200)),
                ('food_restaurant_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
