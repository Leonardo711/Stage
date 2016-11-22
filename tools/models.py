from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tool(models.Model):
    category_list = (
        '团队数据共享',
        '站外数据库',
        '常用分析工具',
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_list)
    content = models.TextField()
