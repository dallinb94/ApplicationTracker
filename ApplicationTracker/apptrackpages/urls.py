from django.urls import path
from .views import indexPageView, applicationsPageView, applicationsEditPageView, applicationsAddPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('applications/', applicationsPageView, name='applications'),
    path('edit/', applicationsEditPageView, name='edit'),
    path('add/', applicationsAddPageView, name='add'),
]