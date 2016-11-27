from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from notice.models import *
from notice.forms import NoticeForm
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class noticeList(ListView):
    model=Notice
    template_name = "notice/noticeList.html"
    context_object_name = 'notice_list'

class noticeDetail(DetailView):
    model = Notice
    template_name = "notice/noticeDetail.html"
    context_object_name = "notice"

    def get(self, request, *args, **kwargs):
        self.object = Notice.objects.get(id=kwargs['id'])
        notice = Notice.objects.get(id=kwargs['id'])
        self.object.viewed()
        return self.render_to_response(self.get_context_data(notice=notice))

class noticeAdd(PermissionRequiredMixin, CreateView):
    permission_required = 'notice.add_notice'
    model = Notice
    template_name = "notice/noticeAdd.html"
    form_class = NoticeForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.form_class)
        if form.is_valid():
            form.save()
