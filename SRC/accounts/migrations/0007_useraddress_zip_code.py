# Generated by Django 3.2.9 on 2021-12-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211226_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='zip_code',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
