#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Meeting(models.Model):
    name = models.CharField(_('meeting name'),max_length=100)
    date = models.DateField(_("meeting time"))
    content = models.TextField(_("meeting content"))

    class Meta:
        ordering=['-date']
        verbose_name=_("meeting")
        verbose_name_plural= _("meetings")
