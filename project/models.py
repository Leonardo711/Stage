from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=20,primary_key=True)
    basicInformation = models.TextField()
    article_outside = models.CharField(max_length=100)


    class Meta:
        ordering = ['category']

    def __unicode__(self):
        return self.name
