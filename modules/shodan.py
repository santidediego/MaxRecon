from imports import *

SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

def init_shodan():
    print(colored.green("\n##########################"))
    print(colored.green("\nWelcome to Shodan module\n"))
    print(colored.green("##########################\n"))

def show_shodan_options():
    print("\nChoose an option:")
    print("1) Manual Search:")
    print("2) Information about a single target")
    print("3) Search for webcams")
    print("4) Back")
    print("Choose an option: ")

def manual_request(query):
    try:
        # Search Shodan
        results = api.search(query)
        # Show the results
        print(colored.red("\n-----------------------------------"))
        print(colored.red("\nResults found: %s" % results['total'])+"\n")

        for result in results['matches']:
            print(colored.green("IP: %s" % result['ip_str']))
            print(colored.green("Country: %s" % result['location']['country_name']))
            print(colored.green("City: %s" % result['location']['city']))
            print(colored.yellow("Latitude: %s" % result['location']['latitude']))
            print(colored.yellow("Longitude: %s" % result['location']['longitude']))
            print(colored.cyan("\nInformation:\n"))
            print(result['data'])
            print('')

    except:
        print (colored.red("Query error"))

def single_target(address):
    try:
        # Lookup the host
        host = api.host(address)

        # Print general info
        print("\n")
        print(colored.red("--------------------------------"))
        print(colored.red("\nInformation:\n"))
        print(colored.green("IP: %s" % host['ip_str']))
        print(colored.green("Organization: %s" % host.get('org', 'n/a')))
        print(colored.green("Operating System: %s" % host.get('os', 'n/a')))
        print(colored.yellow("\nPorts:\n"))
        for item in host['data']:
            print(colored.yellow("Port %s" % item['port']))
            print("Banner:\n %s" % item['data'])

    except:
        print(colored.red("\nNo information was found about this IP"))

def search_webcams():
    try:
        # Search Shodan
        results = api.search('Server: SQ-WEBCAM')
        # Show the results
        print(colored.red("\n-----------------------------------"))
        print(colored.red("\nResults found: %s" % results['total'])+"\n")

        for result in results['matches']:
            print(colored.green("IP: %s" % result['ip_str']))
            print(colored.green("Country: %s" % result['location']['country_name']))
            print(colored.green("City: %s" % result['location']['city']))
            print(colored.yellow("Latitude: %s" % result['location']['latitude']))
            print(colored.yellow("Longitude: %s" % result['location']['longitude']))
            print(colored.cyan("\nInformation:\n"))
            print(result['data'])
            print('')

    except:
        print (colored.red("Query error"))

def shodan_hacking():
    init_shodan()
    option=0
    while option!='4':
        show_shodan_options()
        option = input()
        if option == '1':
            print("\nWrite your query")
            query = input()
            manual_request(query)
        elif option == '2':
            address = ask_for_address()
            single_target(address)
        elif option == '3':
            search_webcams()
