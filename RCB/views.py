from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Virat(request):
    return HttpResponse('<h1>Virat is the Best Batsman in Current Era!!!!!!!!!!!</h1>')

def ABD(request):
    return HttpResponse('<h1>ABD is known as MR.360 & He is a Monster!!!!!!!!!! </h1>')