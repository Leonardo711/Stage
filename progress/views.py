from django.shortcuts import render

# Create your views here.
def testView(request):
    return render(request, template_name="progress/progressBase.html")
