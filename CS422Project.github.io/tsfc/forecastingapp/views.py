import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from .models import File
from .forms import FileUploadForm
import uuid
from django.template.defaultfilters import filesizeformat

def say_sth(request):
    return render(request, 'index.html', {'name': 'Team 2!!!'})

#def linkto_detail(request):
    #return render(request, 'link.html')

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

# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'forecastingapp/templates/filelist.html', {'files': files})


def file_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get cleaned data
            upload_method = form.cleaned_data.get("upload_method")
            raw_file = form.cleaned_data.get("file")
            new_file = File()
            new_file.file = handle_uploaded_file(raw_file)
            new_file.upload_method = upload_method
            new_file.save()
            return redirect("/file/")
    else:
        form = FileUploadForm()

    return render(request, 'forecastingapp/templates/upload_form.html', 
                  {'form': form, 'heading': 'Upload files with Regular Form'}
                 )

def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    # file path relative to 'media' folder
    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path


