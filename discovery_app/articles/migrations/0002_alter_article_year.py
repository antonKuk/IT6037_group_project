# Generated by Django 4.1.1 on 2022-09-08 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinLengthValidator(2022)]),
        ),
    ]