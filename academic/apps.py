from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AcademicConfig(AppConfig):
    name = 'academic'
    verbose_name = _("Academics")

