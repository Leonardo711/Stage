#-*-coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext as _

# Create your models here.
class News(models.Model):
    title = models.CharField(_('news title'),max_length = 100)
    pub_time = models.DateTimeField(_('publish time'), auto_now_add=True)
    content = RichTextUploadingField(_('news content'))
    views = models.IntegerField(_('viewed'), default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("news author"), on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
        verbose_name= _("news")
        verbose_name_plural = _("news")

    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs={'pk':self.id})

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])


