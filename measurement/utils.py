import geoip2
from django.contrib.gis.geoip2 import GeoIP2
def get_location(ip):
    g=GeoIP2()
    country=g.country(ip)
    city=g.city(ip)
    lat,lon=g.lat_lon(ip)
    return country,city,lat,lon