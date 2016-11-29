#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Tool(models.Model):
    category_list = (
        ('data sharing in team','team'), #团队数据共享
        ('databases','outside'), #站外数据库
        ('basic tools','usual'), # 常用数据工具
    )
    category = models.CharField(max_length=20, choices=category_list, primary_key=True)
    content = models.TextField()
