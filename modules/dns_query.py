from imports import *

def dns_query():
    address=ask_for_domain()
    try:
        direction=dns.resolver.query(address, "A")
        print ("\nA recorder:")
        print ("-----------------------------------------")
        print(direction.response.to_text())
    except:
        print("\nYour domain´s name hasn´t got A register or is empty\n")

    try:
        direction=dns.resolver.query(address, "MX")
        print ("MX recorder:")
        print ("-----------------------------------------")
        print(dirMX.response.to_text())
    except:
        print("\nYour domain´s name hasn´t got MX register or is empty\n")
    try:
        direction=dns.resolver.query(address, "NS")
        print ("NS recorder:")
        print ("-----------------------------------------")
        print(dirNS.response.to_text())
    except:
        print("\nYour domain´s name hasn´t got NS register or is empty \n")
    try:
        direction=dns.resolver.query(address, "AAAA")
        print ("AAAAA recorder:")
        print ("-----------------------------------------")
        print(dirAAAA.response.to_text())
    except:
        print("\nYour domain´s name hasn´t got AAAA register or is empty\n")

    #To do: zone Transfer
    print("\n<Continue>\n")
    input()
