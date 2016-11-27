from django.conf.urls import url, include
from academic.views import *

urlpatterns = [
    url(r'^$', academicList.as_view(), name="academicView"),
]
