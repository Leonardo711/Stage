#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tool(models.Model):
    category_list = (
        ('团队数据共享','team'),
        ('站外数据库','outside'),
        ('常用分析工具','usual'),
    )
    category = models.CharField(max_length=20, choices=category_list, primary_key=True)
    content = models.TextField()
