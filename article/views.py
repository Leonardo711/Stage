from django.shortcuts import render
from django.views.generic import TemplateView
from article.models import *

# Create your views here.
class articleArchive(TemplateView):
    model = article_publish
    template_name = "article/articleBase.html"

    def get(self, request, *args, **kwargs):
        articleList = article_publish.objects.all()
        yearSet = set()
        for article in articleList:
            yearSet.add(article.pub_time.year)
        yearList = sorted(yearSet, reverse=True)
        return self.render_to_response(self.get_context_data(articleList=articleList, yearList=yearList))



