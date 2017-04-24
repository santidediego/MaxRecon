from imports import *

def show_options():
        print("\nChoose an option:")
        print("1) Ask the DNS Server")
        print("2) WHOIS Information")
        print("3) Geolocate the target")
        print("4) Google Hacking")
        print("5) Metadata analysis in PDF files")
        print("6) Scan the target")
        print("7) Scan for webcams in a local network")
        print("8) Shodan Hacking")
        print("9) Exit")
        print("Choose an option: ")


def init_shodan():
    print("\nWelcome to Shodan module\n")

def show_shodan_options():
    print("\nChoose an option:")
    print("1) Manual Search:")
    print("2) Information about a single target")
    print("3) Search for webcams")
    print("4) Back")
    print("Choose an option: ")

def domain_or_ip():
    print("\nWhat do you want to use?")
    print("1) IP")
    print("2) Domain name")
    option=input()

    if option=='1':
        address=ask_for_address()
        return address
    elif option=='2':
        address=ask_for_domain()
        return address
    else:
        print("\nPlease select a valid option")
        return


def ask_for_domain():
    print("\nWrite the target domain: ")
    address=input()
    return address

def ask_for_address():
    print("\nWrite the target IP address: ")
    address=input()
    return address

def ask_for_network():
    print("\nWrite a valid network,domain or IP address: ")
    address=input()
    return address

def ask_for_pdf():
    print("\nWrite the pdf file path, with extension included: ")
    pdf=input()
    return pdf
