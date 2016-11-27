from django.conf.urls import url, include
from progress.views import *

urlpatterns = [
    url(r'^$', progressListView.as_view(), name="academicView"),
]
