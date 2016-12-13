#! /usr/bin/env python
'''


'''

import dns
import dns.resolver
import whois
import pygeoip
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import nmap
import os

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def domain_or_ip():
    print("What do you want to use?")
    print("1) IP")
    print("2) Domain name")
    option=input()
    for case in switch(option):
        if case('1'):
            ask_for_address()
            break
        if case('2'):
            ask_for_domain()
            break
        if case():
            print("Please select a correct option")


def ask_for_domain():
    print("Write the target domain: ")
    address=input()
    return address

def ask_for_address():
    print("Write the target IP address: ")
    address=input()
    return address

def ask_for_pdf():
    print("Write the pdf file path: ")
    pdf=input()
    return pdf

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

    #Transferencia de zona
    print("\n<Continue>\n")
    input()

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

def geolocate():
    country = pygeoip.GeoIP('Data/GeoIP.dat')
    city = pygeoip.GeoIP('Data/GeoLiteCity.dat')
    address=ask_for_address()
    try:
        print("Country: "+country.country_name_by_addr(address) + "Code: "+country.country_code_by_addr(address))
        print("City: "+city.record_by_addr(address))
    except:
        print("No valid IP, something was wrong")
        return
    print("\n<Continue>\n")
    input()

def googlehacking():
    print("\n")
    print("Welcome to google hacking tool. GoogleDB-tool.py will be used in the background. Results will be saved in reports directory")
    address=domain_or_ip()
    print ("Select an option:")
    print("1) Vulnerabilities")
    print("2) Login pages")
    print("3) Interesting directories")
    print("4) SQL injection list")
    print("5) All")
    print("Choose an option: ")
    option=input()
    for case in switch(option):
        if case('1'):
            os.system("python scripts/googleDB-tool.py vulnerabilities.txt -s "+address+" -o reports/output_vul.txt ")
            break
        if case('2'):
            os.system("python scripts/googleDB-tool.py login_pages.txt -s "+address+" -o reports/output_logins.txt ")
            break
        if case('3'):
            os.system("python scripts/googleDB-tool.py interesting_directories.txt -s "+address+" -o reports/output_directories.txt ")
            break
        if case('4'):
            os.system("python scripts/googleDB-tool.py sql_injection_list.txt -s "+address+" -o reports/output_sql-injection.txt ")
            break
        if case('5'):
            os.system("python scripts/googleDB-tool.py vulnerabilities.txt -s "+address+" -o reports/output_vul.txt ")
            os.system("python scripts/googleDB-tool.py login_pages.txt -s "+address+" -o reports/output_logins.txt ")
            os.system("python scripts/googleDB-tool.py interesting_directories.txt -s "+address+" -o reports/output_directories.txt ")
            os.system("python scripts/googleDB-tool.py sql_injection_list.txt -s "+address+" -o reports/output_sql-injection.txt ")
            break
        if case():
            print("Please, select a correct option")
            return
    print("\nFile(s) correctly saved in reports/")
    print("\n<Continue>\n")
    input()

def metadata():
    path=ask_for_pdf()
    try:
        pdfFile=PdfFileReader(open(path,'rb'))
    except:
        print("No pdf was found")
        return
    metadatas=pdfFile.getDocumentInfo()
    print("\nMetadatas:")
    print("----------------------------")
    for data in metadatas:
        print("[+]"+data+ ":"+metadatas[data])

    print("\n<Continue>\n")
    input()


def silent_scan(address):
    nm = nmap.PortScanner()
    print("\nScanning, be patient\n")
    nm.scan(hosts=address, arguments='-n -sS -sV')
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


def intensive_scan(address):
    nm = nmap.PortScanner()
    print("\nScanning, be patient\n")
    nm.scan(hosts=address, arguments='-n -sT -sV')
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

def scan():
    print("\nSelect the kind of scan: ")
    print("1) Silent Scan")
    print("2) Intensive Scan")
    print("3) Custom Scan (nmap must be installed)")
    option=input()
    for case in switch(option):
        if case('1'):
            try:
                address=domain_or_ip()
                silent_scan(address)
            except:
                print("Remind you must run this program as root")
            break
        if case('2'):
            try:
                address=domain_or_ip()
                intensive_scan(address)
            except:
                print("Remind you must run this program as root")
            break
        if case('3'):
            try:
                print("Write your nmap scan. Ex: nmap -sU 8.8.8.8")
                scan=input()
                try:
                    os.system(scan)
                except:
                    print("Scan not correct")
            except:
                print("Remind you must run this program as root")
            break
        if case():
            print("Please, select a valid option")

    print("\n<Continue>\n")
    input()
def main():
    option=0
    while option!='7':
        print("\nChoose an option:")
        print("1) Ask the DNS Server:")
        print("2) WHOIS Information:")
        print("3) Geolocate the target:")
        print("4) Google Hacking:")
        print("5) Metadata analysis in PDF files")
        print("6) Scan the target")
        print("7) Exit")
        print("Choose an option: ")
        option=input()
        for case in switch(option):
            if case('1'):
                dns_query()
                break
            if case('2'):
                whois_query()
                break
            if case('3'):
                geolocate()
                break
            if case('4'):
                googlehacking()
                break
            if case('5'):
                metadata()
                break
            if case('6'):
                scan()
                break
            if case('7'):
                pass
                break
            if case(): # default, could also just omit condition or 'if True'
                option=0

main()
