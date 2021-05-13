from django.db import models

# Create your models here.

class Covid_Observations(models.Model):
    sno = models.PositiveIntegerField(blank=True, null=True)
    observationdate = models.DateField(auto_now=False, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=False, blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)

class CovidData(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    filedata = models.FileField(upload_to='data', max_length=254)