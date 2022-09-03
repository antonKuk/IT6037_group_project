# Generated by Django 4.1 on 2022-09-03 13:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('article_name', models.CharField(max_length=150)),
                ('designed_by', models.CharField(blank=True, max_length=150)),
                ('developer', models.CharField(blank=True, max_length=150)),
                ('dimensions', models.CharField(blank=True, max_length=40)),
                ('about', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('date_born', models.DateField(blank=True)),
                ('date_died', models.DateField(blank=True)),
                ('nationality', models.CharField(blank=True, max_length=150)),
                ('known_for', models.CharField(blank=True, max_length=255)),
                ('notable_work', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('medium', models.CharField(blank=True, max_length=150)),
                ('year', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='articles.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='articles.type'),
        ),
    ]