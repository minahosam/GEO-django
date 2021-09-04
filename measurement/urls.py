from django.urls import path
from .views import *
app_name='distance'
urlpatterns = [
    path('',get_distance,name='distnation')
]
