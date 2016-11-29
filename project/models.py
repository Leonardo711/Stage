from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Project(models.Model):
    category = models.CharField(_("category"),max_length=10)
    name = models.CharField(_("species name"), max_length=20,primary_key=True)
    basicInformation = models.TextField(_("basic information"))
    article_outside = models.CharField(_("related articles"),max_length=100)


    class Meta:
        ordering = ['category']

    def __unicode__(self):
        return self.name
