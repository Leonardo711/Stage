from django.shortcuts import render
from collections import OrderedDict
from django.views.generic import TemplateView
from project.models import *

# Create your views here.
class projectView(TemplateView):
    template_name = "project/projectBase.html"

    def get(self, request, *args, **kwargs):
        print(len(request.GET))
        if len(request.GET) == 0:
            projectSet = Project.objects.all()
            print projectSet
            projectDict = OrderedDict()
            for project in projectSet:
                projects = projectDict.setdefault(project.category, [])
                projects.append(project)
            return self.render_to_response(self.get_context_data(projectDict=projectDict))
