from django.shortcuts import render
from .models import *
from .forms import *
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from .utils import *
# Create your views here.
def get_distance(request):
    query=Measurement.objects.get(id=1)
    if request.method=='POST':
        form=measurementForm(request.POST)
        
        if form.is_valid():
            form1=form.save(commit=False)
            destination_=form.cleaned_data['destination']
            global destination
            geolocator=Nominatim(user_agent='measurement')
            ip='156.223.48.186'
            # ip=get_ip(request)
            # print (ip)
            country,city,lat,lon=get_location(ip)
            # print(country,city,lat,lon)
            city_location = geolocator.geocode(city)
            print(city_location)
            l_lat=lat
            l_lon=lon
            pointA=(l_lat,l_lon)
            destination=geolocator.geocode(destination_)
            print(destination)
            d_long=destination.longitude
            d_lat=destination.latitude
            pointB=(d_lat,d_long)
            print(pointB)
            distance1=round(geodesic(pointA , pointB).km , 2)
            m=folium.Map(width = 800,height = 500,location=get_centeralize(l_lat,l_lon,d_lat,d_long),zoom_start=get_zoom(distance1))
            folium.Marker([l_lat,l_lon],tooltip='click here for mor info',popup=city['city'],icon=folium.Icon(color='red',icon="home")).add_to(m)
            folium.Marker([d_lat,d_long],tooltip='click here for more info').add_to(m)
            
            print(distance1)
            # folium.PolyLine([pointA,pointB],weight=5).add_to(m)
            line=folium.PolyLine([pointA,pointB],weight=5,color='orange')
            m.add_child(line)
            m=m._repr_html_()
            form1.location=city_location
            form1.distance=distance1
            form1.save()                                                                                           
    else:
        form=measurementForm()
        geolocator=Nominatim(user_agent='measurement')
        ip='156.223.48.186'
        country,city,lat,lon=get_location(ip)
        # print(country,city,lat,lon)
        city_location = geolocator.geocode(city)
        print(city_location)
        l_lat=lat
        l_lon=lon
        pointA=(l_lat,l_lon)
        print(pointA)
        distance1=None
        destination=None
        
        m=folium.Map(width = 800,height = 500,location=get_centeralize(l_lat,l_lon),zoom_start=8)
        folium.Marker([l_lat,l_lon],tooltip='click here for mor info',popup=city['city'],icon=folium.Icon(color='red',icon="home")).add_to(m)
        m=m._repr_html_()
    # location located in map
    # geolocator=Nominatim(user_agent='measurement')
    # ip='156.223.48.186'
    # country,city,lat,lon=get_location(ip)
    # # print(country,city,lat,lon)
    # city_location = geolocator.geocode(city)
    # print(city_location)
    # l_lat=lat
    # l_lon=lon
    # pointA=(l_lat,l_lon)
    # m=folium.Map(width = 800,height = 500,location=pointA)
    # # location marker
    # folium.Marker([l_lat,l_lon],tooltip='click here for mor info',popup=city['city'],icon=folium.Icon(color='red',icon="home")).add_to(m)
    return render(request,'main/main.html',{'query':query,'form':form ,'map':m,'distance':distance1,'location':city_location,'destination':destination})