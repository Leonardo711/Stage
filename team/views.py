from django.shortcuts import render
from django.views.generic import  ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView
from team.models import *
from collections import OrderedDict
from django.contrib.auth.mixins import PermissionRequiredMixin
from team.forms import *

# Create your views here.
class teamView(TemplateView):
    template_name = "team/teamBase.html"

    def get(self, request, *args, **kwargs):
        print(len(request.GET))
        if len(request.GET) == 0:
            memberSet = Member.objects.filter(priority=0)
            mainMember = Member.objects.filter(priority=1)
            memberDict = OrderedDict()
            for member in memberSet:
                members = memberDict.setdefault(member.teamName, [])
                members.append(member)
            return self.render_to_response(self.get_context_data(mainMember=mainMember, memberDict=memberDict))

class memberAdd(PermissionRequiredMixin, CreateView):
    permission_required = 'notice.add_news'
    model = Member
    template_name = "team/memberAdd.html"
    form_class = MemberForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.form_class)
        if form.is_valid():
            form.save()



