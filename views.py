from django.shortcuts import render
from news.models import *
from team.models import *
from notice.models import Notice
from project.models import *
from django.http import HttpResponse
import simplejson

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

def getContent(request):
    print request.GET
    if request.GET['page'] == 'team':
        member = Member.objects.get(name=request.GET['data_id'])
        response = member.profile
        return HttpResponse(response)
    elif request.GET['page'] =="project":
        outdict = dict()
        project = Project.objects.get(name=request.GET["data_id"])
        outdict['basicInformation'] = project.basicInformation
        outdict['data_id'] = request.GET["data_id"]
        json = simplejson.dumps(outdict)
        return HttpResponse(json)

        return HttpResponse("hello world")
