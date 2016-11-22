from django.shortcuts import render

# Create your views here.
def projectListView(request):
    return render(request, "project/projectBase.html")
