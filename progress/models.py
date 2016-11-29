from __future__ import unicode_literals

from django.db import models
from project.models import Project
from django.utils.translation import ugettext as _

# Create your models here.
class Progress(models.Model):
    project = models.ForeignKey(Project, verbose_name=_("progess"))
    content = models.TextField(_('progress content'))

