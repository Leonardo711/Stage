from django.shortcuts import render
from django.views.generic import TemplateView
from academic.models import Meeting

# Create your views here.
class academicList(TemplateView):
    template_name = "academic/academicBase.html"

    def get(self, request, *args, **kwargs):
        if len(request.GET) == 0:
            meetings = Meeting.objects.all()
            yearSet = set()
            for meeting in meetings:
                yearSet.add(meeting.date.year)
            yearList = sorted(yearSet, reverse=True)
            return self.render_to_response(self.get_context_data(meetings=meetings, yearList=yearList))
