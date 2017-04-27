from imports import *

def check_ids():
    print(colored.cyan("\nThis module will run wafw00f in the background"))
    address=ask_for_address()
    os.system('modules/wafw00f/wafw00f/bin/wafw00f '+address)
    print (colored.yellow("\n<Enter>\n"))
    input()
