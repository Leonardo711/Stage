from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext as _


class ToolsConfig(AppConfig):
    name = 'tools'
    verbose_name = _("Tools")
