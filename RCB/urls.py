from RCB.views import *
from django.urls import path

app_name = 'nothing'

urlpatterns = [
    path('Virat/', Virat, name='Virat'),
    path('ABD/', ABD, name='ABD'),
]
