from __future__ import unicode_literals

from django.db import models
from project.models import Project

# Create your models here.
class Progress(models.Model):
    project = models.ForeignKey(Project)
    content = models.TextField()

