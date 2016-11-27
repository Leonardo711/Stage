from __future__ import unicode_literals

from django.db import models
from project.models import Project

# Create your models here.
class article_publish(models.Model):
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    author = models.CharField(max_length = 20)
    pub_time = models.DateField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.title

