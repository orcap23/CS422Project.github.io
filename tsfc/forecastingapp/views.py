import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
import uuid
from django.template.defaultfilters import filesizeformat

def say_sth(request):
    return render(request, 'index.html', {'name': 'MLE'})


#Handle download train set from the website.
def downloadtrainset(request):
    try:
        file = open('forecastingapp/templates/static/download/train.csv', 'rb')
        response = FileResponse(file)
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename="train.csv"'
        return response
    except Exception as e:
        print(e)
        raise Http404
<<<<<<< HEAD

=======
        
>>>>>>> 3222a7a9f1f6f13e2e6b052a3b7f7074f5dee327
