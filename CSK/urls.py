from CSK.views import *
from django.urls import path
app_name = 'something'

urlpatterns = [
    path('Dhoni/', Dhoni, name='Dhoni'),
    path('Raina/', Raina, name='Raina'),
]
