from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
#from smap.models import contact


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contct.html')


def code(request):
    return render(request, 'code.html')


def note(request):
    return render(request, 'notes.html')


def cpp(request):
    return render(request, 'cpp.html')


def cppch(request):
    return render(request, 'cppch.html')


def java(request):
    return render(request, 'java.html')


def javach(request):
    return render(request, 'javach.html')


def python(request):
    return render(request, 'python.html')


def pythonch(request):
    return render(request, 'pythonch.html')


def paper(request):
    return render(request, 'paper.html')


def notes(request):
    return render(request, 'notes.html')





