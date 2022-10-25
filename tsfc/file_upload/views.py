from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage

# Show file list
def file_list(request):
    #files = File.objects.all().order_by("-id")
    files = File.objects.order_by('-id')   
    return render(request, 'file_list.html', {'files': files})

# Regular file upload without using ModelForm
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

    return render(request, 'upload_form.html', 
                  {'form': form, 'heading': 'Upload files with Regular Form'}
                 )

def delete_file(request, pk): 
    file = File.objects.get(id = pk)
    file.delete()
    return redirect("/file/")
    

def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    # file path relative to 'solutions' folder
    file_path = os.path.join('solutions', file_name)
    absolute_file_path = os.path.join('solutions', 'files', file_name)
   
    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path

