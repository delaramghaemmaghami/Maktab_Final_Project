# Generated by Django 3.2.9 on 2022-01-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_useraddress_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='zip_code',
            field=models.CharField(default=14, max_length=15),
            preserve_default=False,
        ),
    ]
