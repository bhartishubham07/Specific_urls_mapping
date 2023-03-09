from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Dhoni(request):
    return HttpResponse('<marquee><h1>MSD is the Best Finisher in the World!!!!!!!!!!</h1></marquee>')

def Raina(request):
    return HttpResponse('<marquee><h1>Raina is known as MR. IPL!!!!!!!!!!!</h1></marquee>')