from django.urls import path
from .views import landingPageView, showSingleApplicationPageView, applicationsAddPageView, allapplicationsPageView, deleteApplicationPageView
from .views import updateApplicationPageView

urlpatterns = [
    path('applications/<int:application_id>/',
         showSingleApplicationPageView, name='showsingleapplication'),
    path('updateapplication/', updateApplicationPageView, name='update'),
    # path('edit/', applicationsEditPageView, name='edit'),
    path('add/', applicationsAddPageView, name='add'),
    path('', landingPageView, name='landing'),
    path('allapplications/', allapplicationsPageView, name='allapplications'),
    path('delete/<int:application_id>/',
         deleteApplicationPageView, name='delete'),
]
