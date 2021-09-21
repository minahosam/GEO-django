import geoip2
from django.contrib.gis.geoip2 import GeoIP2
def get_location(ip):
    g=GeoIP2()
    country=g.country(ip)
    city=g.city(ip)
    lat,lon=g.lat_lon(ip)
    return country,city,lat,lon
def get_centeralize(latA,longA,latB=None,longB=None):
    core=(latA, longA)
    if  latB:
        core=[(latA+latB)/2 , (longA+longB)/2]
    return core
def get_zoom(distance):
    if distance <= 100:
        return 8
    elif distance > 100 and distance <= 5000 :
        return 4
    else:
        return 2
# def get_ip(request):
#     real_ip=request.META.get('HTTP_X_FORWARDE_FOR')
#     if real_ip:
#         ip=real_ip
#     else:
#         ip=request.META.get('REMOTE_ADDR')
#     return ip