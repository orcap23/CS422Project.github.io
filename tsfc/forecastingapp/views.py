from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction

def say_sth(request):
    return render(request, 'index.html', {'name': 'Team 2!!!'})

def upload_file(request, pk):
    return 0


