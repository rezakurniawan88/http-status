import requests
import argparse
import colorama
from colorama import Fore

parser = argparse.ArgumentParser(description='How to use : http-status.py [options] [url/list]')
parser.add_argument("-u", "--url", help="Scan with single url", default="Need url")
parser.add_argument("-l", "--list", help="Scan with multi url/list file, format(.txt)", default="Need list")
args = parser.parse_args()

ascii_art = """                                                         
 ______ ______ ______ ______ ______ ______ ______ ______ 
|______|______|______|______|______|______|______|______|
 _     _   _                      _        _                
| |   | | | |                    | |      | |               
| |__ | |_| |_ _ __           ___| |_ __ _| |_ _   _ ___    
| '_ \| __| __|  _ \   ____  / __| __/ _` | __| | | / __|   
| | | | |_| |_| |_) | |____| \__ | || (_| | |_| |_| \__ \   
|_| |_|\__|\__| .__/         |___/\__\__,_|\__|\__,_|___/   
              | |                                        
              |_|                                        
 ______ ______ ______ ______ ______ ______ ______ ______ 
|______|______|______|______|______|______|______|______|
                                                  
                                        @rezakurniawan88
"""


# Store urls in an array
urls = []

# If the url argument is empty (Scan via list parameter)
if(args.url == "Need url"):
    lists = args.list
    with open(lists, 'r') as f:
        reads = f.readlines()
        for read in reads:
            urls.append(read.strip())

# If the list argument is empty {Scan via url parameter}
if(args.list == "Need list"):
    urls.append(args.url)

# Looping urls and print the result
def main():
  for url in urls:
      response = requests.get(url)
      if response.status_code == 200:
          print(Fore.GREEN + f"[{response.status_code}]   : {url}")
      elif response.status_code == 403:
          print(Fore.BLUE + f"[{response.status_code}]   : {url}")
      else:
          print(Fore.RED + f"[{response.status_code}]   : {url}")

colorama.init()
print(ascii_art)
print("Starting ...\n")
print("Status  |     Website")
main()
