from django.conf.urls import url, include
from tools.views import *

urlpatterns = [
    url(r'^$', testview, name="tools"),
]
