# Generated by Django 2.1.1 on 2019-01-07 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_booklist', '0001_squashed_0008_auto_20181113_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]+$'), django.core.validators.MinLengthValidator(10)]),
        ),
    ]
