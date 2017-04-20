from imports import *

def silent_scan(address):
    nm = nmap.PortScanner()
    print(colored.green("\nScanning, be patient\n"))
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
    print(colored.green("\nScanning, be patient\n"))
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
    if option=='1':
        try:
            address=domain_or_ip()
            silent_scan(address)
        except:
            print(colored.red("Error: Remind you must run this program as root"))
    elif option=='2':
        try:
            address=domain_or_ip()
            intensive_scan(address)
        except:
            print(colored.red("Error: Remind you must run this program as root"))
    elif option=='3':
        try:
            print("Write your nmap scan. Ex: nmap -sU scanme.nmap.org")
            scan=input()
            try:
                os.system(scan)
            except:
                print("Scan not correct")
        except:
            print(colored.red("Error: Remind you must run this program as root"))
    else:
        print("\nPlease, select a valid option")

    print (colored.yellow("\n<Enter>\n"))
    input()
