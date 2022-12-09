from django.http import HttpResponse
from django.shortcuts import render, redirect
from apptrackpages.models import Application
from .models import Client
from django.conf import settings
from django.db import connection

# Create your views here.


def landingPageView(request):
    return render(request, 'landing.html')


def applicationsPageView(request):
    return render(request, 'apptrackpages/ViewApplication.html')


def allapplicationsPageView(request):
    current_user = request.user
    data = Application.objects.raw(
        'select * from application inner join client ON client.id = application."ApplicationCreator_id" WHERE CLIENT.user_id = %s', [current_user.id])
    context = {
        'app': data
    }
    return render(request, 'apptrackpages/ViewAllApplications.html', context)


def applicationsAddPageView(request):
    current_user = request.user
    client = Client.objects.raw(
        'SELECT id FROM CLIENT WHERE user_id = %s', [current_user.id])
    if request.method == 'POST':
        application = Application()

        application.CompanyName = request.POST['CompanyName']
        application.DateApplied = request.POST['DateApplied']
        application.RecruiterName = request.POST['RecruiterName']
        application.RecruiterEmail = request.POST['RecruiterEmail']
        application.Status = request.POST['Status']
        application.ApplicationNotes = request.POST['ApplicationNotes']
        application.EstimatedSalary = request.POST['EstimatedSalary']
        application.ResumePDF = request.POST['ResumePDF']
        application.ApplicationCreator = Client.objects.get(id=client[0].id)

        application.save()

        return allapplicationsPageView(request)
    else:
        return render(request, 'apptrackpages/addApplication.html')


def deleteApplicationPageView(request, application_id):
    data = Application.objects.get(id=application_id)
    data.delete()
    return allapplicationsPageView(request)


def updateApplicationPageView(request):
    if request.method == 'POST':
        application_id = request.POST['application_id']
        application = Application.objects.get(id=application_id)
        application.CompanyName = request.POST['CompanyName']
        application.DateApplied = request.POST['DateApplied']
        application.RecruiterName = request.POST['RecruiterName']
        application.RecruiterEmail = request.POST['RecruiterEmail']
        application.Status = request.POST['Status']
        application.ApplicationNotes = request.POST['ApplicationNotes']
        application.EstimatedSalary = request.POST['EstimatedSalary']
        application.ResumePDF = request.POST['ResumePDF']

        application.save()
    else:
        return allapplicationsPageView(request)

    return allapplicationsPageView(request)


def showSingleApplicationPageView(request, application_id):
    application = Application.objects.get(id=application_id)
    context = {
        'application': application
    }
    return render(request, 'apptrackpages/editApplication.html', context)
