from imports import *

def domain_or_ip():
    print("What do you want to use?")
    print("1) IP")
    print("2) Domain name")
    option=input()
    for case in switch(option):
        if case('1'):
            address=ask_for_address()
            return address
            break
        if case('2'):
            address=ask_for_domain()
            return address
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

def ask_for_network():
    print("Write a valid network or IP address: ")
    address=input()
    return address

def ask_for_pdf():
    print("Write the pdf file path: ")
    pdf=input()
    return pdf
