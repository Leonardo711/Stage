from django.shortcuts import render
from news.models import *
from team.models import *
from notice.models import Notice
from project.models import *
from tools.models import *
from progress.models import Progress
from django.http import HttpResponse, HttpResponseRedirect
import simplejson
from django.utils import translation


def index(request):
    newsSet = News.objects.all()
    if (len(newsSet)>=3):
        newsSet = newsSet[:3]
    context = {}
    context['newsSet'] = newsSet
    noticeSet = Notice.objects.all()
    if (len(noticeSet)>=3):
        noticeSet = noticeSet[:3]
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
    elif request.GET['page'] == 'progress':
        project = Project.objects.get(name=request.GET["data_id"])
        progress = Progress.objects.get(project=project)
        return HttpResponse(progress.content)
    elif request.GET['page'] == 'tools':
        tool = Tool.objects.get(category=request.GET['data_id'])
        return  HttpResponse(tool.content)

def language(request):
    print request.GET
    if request.GET['language'] == "chinese":
        user_language = "zh-Hans"
    else:
        user_language = "en"
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect("/news/")

