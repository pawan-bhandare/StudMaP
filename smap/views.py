from django.shortcuts import render
from datetime import datetime
from smap.models import Contact,Note
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method =="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact =Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    return render(request, 'contct.html')


def code(request):
    return render(request, 'code.html')


def note(request):
    notes= Note.objects.all()
    n= len(notes)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'notes': notes}
    return render(request, 'notes.html',params)


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





