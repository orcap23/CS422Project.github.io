from django.db import models

#https://docs.djangoproject.com/en/4.1/topics/db/models/
#https://stackoverflow.com/questions/17821400/regex-match-for-domain-name-in-django-model

#model will handle the table after upload the file, I will finish it on Friday I believe.
#The table needs to update each time after upload.
#First row will be like Upload_Name, MAE, MAPE,....
#Table needs to be show on the second page after MLE click the link in the main page.
#The main page needs to have a table contain TS_name, Link.

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










    