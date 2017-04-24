from imports import *

SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

def manual_request(query):
    try:
        # Search Shodan
        results = api.search(query)
        # Show the results
        print(colored.green("\n-----------------------------------"))
        print(colored.green("\nResults found: %s" % results['total'])+"\n")
        print(results)
        for result in results['matches']:
            print(colored.green("IP: %s" % result['ip_str']))
            print(colored.green("Country: %s" % result['location']['country_name']))
            print(colored.green("City: %s" % result['location']['city']))
            print(colored.yellow("Latitude: %s" % result['location']['latitude']))
            print(colored.yellow("Longitude: %s" % result['location']['longitude']))
            '''
            print(colored.green("\nPorts:\n"))
            for item in result['data']:
                print(
                    """
                                Port: %s
                    """ % item['port']
                )
                '''
            print("\nInformation:\n")
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
    init_shodan()
    option=0
    while option!='3':
        show_shodan_options()
        option = input()
        if option == '1':
            print("\nWrite your query")
            query = input()
            manual_request(query)
        elif option == '2':
            address = ask_for_address()
            single_target(address)



