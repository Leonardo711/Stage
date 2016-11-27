from django.conf.urls import url
from django.contrib import admin
from team.views import *


urlpatterns = [
    url(r'^$', teamView.as_view(), name="member_list"),
    url(r'^add', memberAdd.as_view(), name="member_add"),
]
