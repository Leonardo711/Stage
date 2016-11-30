#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.utils.translation import  ugettext as _

# Create your models here.
class Tool(models.Model):
    category_list = (
        ('团队数据共享',_('team')), #团队数据共享
        ('站外数据库',_('outside')), #站外数据库
        ('常用数据工具',_('usual')), # 常用数据工具
    )
    category = models.CharField(max_length=20, choices=category_list, primary_key=True)
    content = models.TextField()

    def __unicode__(self):
        return self.category