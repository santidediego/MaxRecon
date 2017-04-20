
#! /usr/bin/env python
'''
Author: Santiago de Diego

This program scans a network looking for security cameras which usually run in ports specified
You can set the variable "ports" in order to modify this
Ports have been extracted from Shodan

'''
from imports import *


def cam_detector(net):
    ports='80,81,82,88,1234,7547,8000,8080'
    objetives=[]
    print("Hosts selected: "+net)
    nm=nmap.PortScanner()
    results=nm.scan(hosts=net, arguments='-sV -O -sT -p '+ports) #Scanning the most common ports for cams
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if nm[host][proto][port]['state']=='open':
                    objetives.append(host)
                    break

    if len(objetives)==0:
        print(colored.red("\nNo security cameras were found in this network, you might add more ports\n"))
    else:
        for host in objetives:
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
               print('----------')
               print('Protocol : %s' % proto)
               lport = nm[host][proto].keys()
               for port in lport:
                   print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

def cam():
    address=ask_for_network()
    try:
        cam_detector(address)
    except:
        print(colored.red("Error: Remind you must run this program as root"))
    print (colored.yellow("\n<Enter>\n"))
    input()
