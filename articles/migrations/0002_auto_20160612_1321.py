# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='add_date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='coment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles'),
        ),
    ]