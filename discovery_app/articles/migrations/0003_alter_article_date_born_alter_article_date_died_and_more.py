# Generated by Django 4.1.1 on 2022-09-08 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_born',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2022)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_died',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2022)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2022)]),
        ),
    ]