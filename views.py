from django.shortcuts import render
from news.models import News
from notice.models import Notice

def index(request):
    newsSet = News.objects.all()
    if (len(newsSet)>=3):
        newsSet = newsSet[:2]
    context = {}
    context['newsSet'] = newsSet
    noticeSet = Notice.objects.all()
    if (len(noticeSet)>=3):
        noticeSet = noticeSet[:2]
    context['noticeSet'] = noticeSet
    return render(request, "index.html", context)
