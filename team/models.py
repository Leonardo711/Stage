from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    teamName = models.CharField(max_length=20)
    priority = models.IntegerField() # main Team or not
    profile = models.TextField()

    class Meta:
        ordering=['-priority']
