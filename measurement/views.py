from django.shortcuts import render
from .models import *
from .forms import *
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import *
# Create your views here.
def get_distance(request):
    query=Measurement.objects.get(id=1)
    if request.method=='POST':
        form=measurementForm(request.POST)
        geolocator=Nominatim(user_agent='measurement')
        ip='102.42.184.233'
        country,city,lat,lon=get_location(ip)
        # print(country,city,lat,lon)
        city_location = geolocator.geocode(city)
        print(city_location)
        l_lat=lat
        l_lon=lon
        pointA=(l_lat,l_lon)
        print(pointA)
        if form.is_valid():
            form1=form.save(commit=False)
            destination_=form.cleaned_data['destination']
            destination=geolocator.geocode(destination_)
            print(destination)
            d_long=destination.longitude
            d_lat=destination.latitude
            pointB=(d_lat,d_long)
            print(pointB)
            distance1=round(geodesic(pointA , pointB).km , 2)
            print(distance1)
            form1.location=city_location
            form1.distance=distance1
            form1.save()
    else:
        form=measurementForm()
    return render(request,'main/main.html',{'query':query,'form':form})