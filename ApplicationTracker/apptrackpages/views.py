from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render(request, 'apptrackpages/ViewAllAPplications.html')

def applicationsPageView(request) :
    return render(request, 'apptrackpages/ViewApplicaiton.html')


def applicationsEditPageView(request) :
    return render(request, 'apptrackpages/editApplication.html')

def applicationsAddPageView(request) :
    return render(request, 'apptrackpages/addApplication.html')

def loginPageView(request) :
    return render(request, 'apptrackpages/login.html')

# create new views when we learn the perameters
# Connor made this edit
# make sure to include a gitignore file