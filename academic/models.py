from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Meeting(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()

    class Meta:
        ordering=['-date']
