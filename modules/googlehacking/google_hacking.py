
from imports import *

def init_google():
    print (colored.green("\n#########################################"))
    print (colored.green("##### Welcome to Google Hacking module#####"))
    print (colored.green("###########################################\n"))

def show_google_options():
    print("Choose an option: ")
    print ("1) Search for directories")
    print ("2) Search for configuration files")
    print ("3) Search for databases")
    print ("4) Search for exposed log files")
    print ("5) Search for exposed backup files")
    print ("6) Search for login pages")
    print ("7) Search for SQL vulnerabilities")
    print ("8) Search for exposed doc files")
    print ("9) Search for php_info")
    print ("10) Back")

def googlehacking():
    init_google()
    option = 0
    while option != '10':
        show_google_options()
        option=input()
        if option=='1':
            address = domain_or_ip()
            query = "site:" + address + " intitle:index.of"
            print(query)
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass
        elif option=='2':
            address = domain_or_ip()
            query = "site:" + address + " ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass
        elif option=='3':
            address = domain_or_ip()
            query = "site:" + address + " ext:sql | ext:dbf | ext:mdb"
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        elif option=='4':
            address = domain_or_ip()
            query = "site:"+address+" ext:log"
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        elif option=='5':
            address = domain_or_ip()
            query = "site:"+address+" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        elif option=='6':
            address = domain_or_ip()
            query = "site:"+address+" inurl:login"
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        elif option == '7':
            address = domain_or_ip()
            query = 'site:'+address+' intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        elif option == '8':
            address = domain_or_ip()
            query = 'site:'+address+' ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        elif option == '9':
            address = domain_or_ip()
            query = 'site:'+address+' ext:php intitle:phpinfo "published by the PHP Group"'
            try:
                for url in search(query, stop=40):
                    print(url)
            except:
                pass

        else:
            print("Please, select a correct option")
