from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Line

# Create your views here.
from django.http import HttpResponse
def foo(request):
   return render_to_response("helloDJ/home.html",
                             {"Testing" : "Django Template Inheritance",
                             "HelloHello" : "Hello World - Django",
                             "lines" : Line.objects.all()})
def home(request, name):
    place = models.Place.objects.get(name__iexact=name)