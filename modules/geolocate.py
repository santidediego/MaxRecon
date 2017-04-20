
from imports import *

def geolocate():
    country = pygeoip.GeoIP('Data/GeoIP.dat')
    city = pygeoip.GeoIP('Data/GeoLiteCity.dat')
    address=ask_for_address()
    try:
        print("\nCountry:\n")
        print(country.country_name_by_addr(address) + "Code: "+country.country_code_by_addr(address)+"\n")
        print("\nCity:\n")
        pprint.pprint(city.record_by_addr(address))
    except:
        print("No valid IP, something was wrong")
        return
    print (colored.yellow("\n<Enter>\n"))
    input()
