# Generated by Django 3.0.3 on 2020-09-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20200922_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(),
        ),
    ]
