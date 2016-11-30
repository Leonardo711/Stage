from __future__ import unicode_literals

from django.db import models
from project.models import Project
from django.utils.translation import ugettext as _

# Create your models here.
class Progress(models.Model):
    project = models.ForeignKey(Project, verbose_name=_("project"))
    content = models.TextField(_('progress content'))

    class Meta:
        verbose_name = _("progress")
        verbose_name_plural = _("progress")
