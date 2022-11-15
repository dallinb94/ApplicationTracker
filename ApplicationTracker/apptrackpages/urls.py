from django.urls import path
from .views import indexPageView, applicationsPageView, applicationsEditPageView, applicationsAddPageView, loginPageView

urlpatterns = [
    path('applications/', applicationsPageView, name='applications'),
    path('edit/', applicationsEditPageView, name='edit'),
    path('add/', applicationsAddPageView, name='add'),
    path('login/', loginPageView, name='login'),
    path('', indexPageView, name='index'),
]