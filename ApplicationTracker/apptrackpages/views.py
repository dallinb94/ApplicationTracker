from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('This is the index page')

def applicationsPageView(request) :
    return HttpResponse('This is where you see applications')

def applicationsEditPageView(request) :
    return HttpResponse('This is where you can edit your applications')

def applicationsAddPageView(request) :
    return HttpResponse('This is where you can add applications')