from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Homepage(request):
    return render(request,'first_app\Homepage.html' )

def Index(request):
    return render(request,'first_app\Index.html' )