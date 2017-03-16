
from imports import *

def whois_query():
    address=ask_for_domain()
    try:
        search = whois.whois(address)
    except:
        print("Error reading your domain. Example: google.com")
        return
    print(search.text)
    print("<Continue>")
    input()
