from django.conf.urls import url, include
from project.views import *

urlpatterns = [
    url(r'^$', projectListView, name="project_list"),
]
