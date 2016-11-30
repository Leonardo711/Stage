from __future__ import unicode_literals

from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _

class ProgressConfig(AppConfig):
    name = 'progress'
    verbose_name = _("Progress")
