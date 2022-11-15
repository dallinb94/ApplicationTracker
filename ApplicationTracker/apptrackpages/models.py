from django.db import models
from datetime import datetime




# Create your models here.

class testDummy(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)



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
    ApplicationCreator = models.ForeignKey(testDummy, on_delete=models.CASCADE, blank=True)
