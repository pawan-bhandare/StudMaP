
from django.urls import path,include
from . import views

urlpatterns = [
path("",views.index, name="StudMap"),
path("about/",views.about,name="about"),
path("contact/",views.contact,name="contact"),
path("code/",views.code,name="code"),
path("note/",views.note,name="note"),
path("cpp/",views.cpp,name="cpp"),
path("cppch/",views.cppch,name="cppch"),
path("java/",views.java,name="java"),
path("javach/",views.javach,name="javach"),
path("python/",views.python,name="python"),
path("pythonch/",views.pythonch,name="pythonch"),
path("paper/",views.paper,name="paper"),
path("notes/",views.notes,name="notes")









]
