from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from tools.models import Tool

# Create your views here.
def testview(request):
    return render(request, template_name="tools/toolsBase.html")
class toolsList(TemplateView):
    template_name = "tools/toolsBase.html"

    def get(self, request, *args, **kwargs):
        if len(request.GET) == 0:
            toolsSet = Tool.objects.all()
            return self.render_to_response(self.get_context_data(toolsSet=toolsSet))

