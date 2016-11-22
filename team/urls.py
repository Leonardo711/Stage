from django.conf.urls import url
from django.contrib import admin
from team.views import *


urlpatterns = [
    url(r'^$', teamListView, name="member_list"),
]
