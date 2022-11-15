from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    indentifier = models.CharField(max_length=40, unique=True)


    USERNAME_FIELD = 'indentifier'


class Application (models.Model):
    CompanyName= models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    DateApplied = models.DateField(default=datetime.today, blank=True)
    RecruiterName = models.CharField(max_length=30)
    RecruiterEmail = models.EmailField(max_length=254)
    Status = models.CharField(max_length=200)
    ApplicationNotes = models.CharField(max_length=1000, blank=True)
    EstimatedSalary = models.DecimalField(max_digits=9, decimal_places=2,blank=True)
    ResumePDF = models.FileField( upload_to='uploads/', blank=True)
    ApplicationCreator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
