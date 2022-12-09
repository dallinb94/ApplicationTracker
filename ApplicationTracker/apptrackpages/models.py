from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Client(models.Model):
    @receiver(post_save, sender=User)
    def create_Client(sender, instance, created, ** kwargs):
        if created:
            Client.objects.create(user=instance)

    class Meta:
        db_table = 'client'
        verbose_name_plural = "clients"
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.firstName))


class Application (models.Model):
    class Meta:
        db_table = 'application'
        verbose_name_plural = "applications"
    CompanyName = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    DateApplied = models.DateField(default=datetime.today, blank=True)
    RecruiterName = models.CharField(max_length=30)
    RecruiterEmail = models.EmailField(max_length=254)
    Status = models.CharField(max_length=200)
    ApplicationNotes = models.CharField(max_length=1000, blank=True)
    EstimatedSalary = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True)
    ResumePDF = models.FileField(upload_to='uploads/', blank=True)
    ApplicationCreator = models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return (str(self.CompanyName))
