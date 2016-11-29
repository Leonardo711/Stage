from __future__ import unicode_literals

from django.db import models
from project.models import Project
from django.utils.translation import ugettext as _

# Create your models here.
class article_publish(models.Model):
    title = models.CharField(_('article title'), max_length=200)
    href = models.CharField(_('article link'), max_length=2000)
    author = models.CharField(_('article authors'),max_length = 200)
    pub_time = models.DateField(_("publish date"))
    project = models.ForeignKey(Project, verbose_name=_("project belong to"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("article by team members")
        verbose_name_plural = _("articles by team members")
