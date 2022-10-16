from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from django.db import transaction
=======

>>>>>>> 005d403 (model changed)

def say_sth(request):
    return render(request, 'index.html', {'name': 'Team 2!!!'})

def upload_file(request, pk):
    return 0


