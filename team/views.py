from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from team.models import *

# Create your views here.
def teamListView(request):
    return render(request, template_name="team/teamBase.html")

