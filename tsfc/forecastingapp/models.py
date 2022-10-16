from django.db import models

#https://docs.djangoproject.com/zh-hans/4.1/topics/db/models/
#https://stackoverflow.com/questions/17821400/regex-match-for-domain-name-in-django-model

class Tsmetadata(models.Model):
    tsname = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    domain = models.CharField(max_length=255)
    units = models.IntegerField()
    keywords = models.CharField(max_length=255)
    scalar = models.IntegerField()
    Length = models.IntegerField()
    SamplingPeriod = models.DecimalField(max_digits=6, decimal_places=2)

class Tsdata(models.Model):
    date = models.DateField(null=True)
    time = models.IntegerField()
    magnitude = models.DecimalField(max_digits=6, decimal_places=2)
    tstime = models.OneToOneField(Tsmetadata, on_delete=models.CASCADE)










    