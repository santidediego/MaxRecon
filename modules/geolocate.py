
from imports import *

def geolocate():
    country = pygeoip.GeoIP('Data/GeoIP.dat')
    city = pygeoip.GeoIP('Data/GeoLiteCity.dat')
    address=ask_for_address()
    try:
        print(colored.green("\nCountry: "+country.country_name_by_addr(address)))
        print(colored.green("City: %s" % city.record_by_addr(address)['city']))
        print(colored.yellow("Latitude: %s" % city.record_by_addr(address)['latitude']))
        print(colored.yellow("Longitude: %s" % city.record_by_addr(address)['longitude']))
    except:
        print(colored.red("\nNo valid IP, something was wrong\n"))
        return
    print (colored.yellow("\n<Enter>\n"))
    input()
