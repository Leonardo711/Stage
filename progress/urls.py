from django.conf.urls import url, include
from progress.views import *

urlpatterns = [
    url(r'^$', testView, name="academicView"),
]
