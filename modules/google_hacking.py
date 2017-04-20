
from imports import *

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
    if option=='1':
        command=os.system("python scripts/googleDB-tool.py vulnerabilities.txt -s "+address+" -o reports/output_vul.txt ")
    elif option=='2':
        command=os.system("python scripts/googleDB-tool.py login_pages.txt -s "+address+" -o reports/output_logins.txt ")
    elif option=='3':
        command=os.system("python scripts/googleDB-tool.py interesting_directories.txt -s "+address+" -o reports/output_directories.txt ")
    elif option=='4':
        command=os.system("python scripts/googleDB-tool.py sql_injection_list.txt -s "+address+" -o reports/output_sql-injection.txt ")
    elif option=='5':
        command=os.system("python scripts/googleDB-tool.py vulnerabilities.txt -s "+address+" -o reports/output_vul.txt ")
        command=os.system("python scripts/googleDB-tool.py login_pages.txt -s "+address+" -o reports/output_logins.txt ")
        command=os.system("python scripts/googleDB-tool.py interesting_directories.txt -s "+address+" -o reports/output_directories.txt ")
        command=os.system("python scripts/googleDB-tool.py sql_injection_list.txt -s "+address+" -o reports/output_sql-injection.txt ")
    else:
        print("Please, select a correct option")
        return
    print("\nFile(s) correctly saved in reports/")
    print (colored.yellow("\n<Enter>\n"))
    input()
