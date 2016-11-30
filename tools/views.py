from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from tools.models import Tool

# Create your views here.
class toolsList(TemplateView):
    template_name = "tools/toolsBase.html"

    def get(self, request, *args, **kwargs):
        print request.GET
        if len(request.GET) == 0:
            toolsSet = Tool.objects.all()
            print toolsList
            return self.render_to_response(self.get_context_data(toolsSet=toolsSet))

