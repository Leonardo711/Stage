from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    parentClass = models.CharField(max_length=10)
    name = models.CharField(max_length=20,primary_key=True)
    basicInformation = models.TextField()
    database = models.ForeignKey()
    article_publish = models.ForeignKey()
    article_outside = models.CharField()


    class Meta:
        ordering = ['parentClass']
