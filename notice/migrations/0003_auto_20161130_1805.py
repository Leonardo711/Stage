# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-30 10:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20161127_0541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-pub_time'], 'verbose_name': 'notice', 'verbose_name_plural': 'notices'},
        ),
        migrations.AlterField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name='notice content'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='publish time'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=100, verbose_name='notice title'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='views',
            field=models.IntegerField(default=0, verbose_name='viewed'),
        ),
    ]
