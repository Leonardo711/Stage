from django.conf.urls import url, include
from article.views import *

urlpatterns = [
    url(r'^$', articleArchive.as_view(), name="article_archieve"),
]
