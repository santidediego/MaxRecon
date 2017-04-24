from imports import *

SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

def manual_request(query):
    try:
        # Search Shodan
        results = api.search(query)
        # Show the results
        print("\n-----------------------------------")
        print("\nResults found: %s" % results['total'])
        for result in results['matches']:
            print("IP: %s" % result['ip_str'])
            print(result['data'])
            print('')
    except:
        print (colored.red("Query error"))

def single_target(address):
    try:
        # Lookup the host
        host = api.host(address)

        # Print general info
        print(
        """
                IP: %s
                Organization: %s
                Operating System: %s
        """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))
        )

        # Print all banners
        for item in host['data']:
            print(
            """
                        Port: %s
                        Banner: %s

                """ % (item['port'], item['data'])
            )
    except:
        print(colored.red("\nNo information was found about this IP"))

def shodan_hacking():
    show_shodan_options()
    option = input()
    if option=='1':
        print("Write your query")
        query=input()
        manual_request(query)
    elif option == '2':
        address=ask_for_address()
        single_target(address)

    elif option=='3':
        pass



