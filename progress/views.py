from django.shortcuts import render
from django.views.generic import TemplateView
from project.models import Project
from progress.models import progress
from collections import OrderedDict

# Create your views here.

class progressListView(TemplateView):
    template_name = "progress/progressBase.html"

    def get(self, request, *args, **kwargs):
        if len(request.GET) == 0:
            projectSet = Project.objects.all()
            projectDict = OrderedDict()
            for project in projectSet:
                projects = projectDict.setdefault(project.category, [])
                projects.append(project)
            firstCat = projectSet.keys()[0]
            first = projectSet[firstCat][0]
            content = progress.objects.get(project=first)
            return self.render_to_response(self.get_context_data(projectDict=projectDict, content=content))
