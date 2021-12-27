# Generated by Django 3.2.9 on 2021-12-27 19:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_useraddress_zip_code'),
        ('restaurant', '0008_auto_20211227_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_address',
            field=models.OneToOneField(blank=True, default=14, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.useraddress'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.CreateModel(
            name='MenuOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order')),
            ],
        ),
    ]
