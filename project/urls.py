from django.conf.urls import url, include
from project.views import *

urlpatterns = [
    url(r'^$', projectView.as_view(), name="project_list"),
]
