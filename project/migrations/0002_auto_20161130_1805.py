# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-30 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='article_outside',
            field=models.CharField(max_length=100, verbose_name='related articles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='basicInformation',
            field=models.TextField(verbose_name='basic information'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=10, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='species name'),
        ),
    ]
