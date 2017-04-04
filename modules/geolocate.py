
from imports import *

def geolocate():
    country = pygeoip.GeoIP('Data/GeoIP.dat')
    city = pygeoip.GeoIP('Data/GeoLiteCity.dat')
    address=ask_for_address()
    try:
        print("Country: "+country.country_name_by_addr(address) + "Code: "+country.country_code_by_addr(address)+"\n")
        print("City: "+str(city.record_by_addr(address)))
    except:
        print("No valid IP, something was wrong")
        return
    print("\n<Enter>\n")
    input()
