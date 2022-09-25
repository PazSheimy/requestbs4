"""
this script is to demonstrate the main factors of request and
how to used it with HTML Parser
HTML Parser to use is beatiful soup
"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys


if __name__ == '__main__':
 # Just to see if the connection worked

#    google = requests.get('https://www.google.com')
#    if google.status_code == 200:
#       print(f"Worked! \n\n{google.content}")
#    elif google.status_code == 404:
#        print("not found")
#   else: print(f"Some Error Ocurred\nError: {google.status_code}")


#using boolean response if google = 200 ture otherwise return false (else)

# google = requests.get('https://www.google.com')
# if google:
#     print(f"Worked! \n\n{google.content}")
# else:
#     print(f"Some Error Ocurred\nError: {google.status_code}")




 for url in sys.argv[1:]:
     #Add https to urls without protocol with layer
     if not url.lower().startswith('http'):
         url = f'https://{url}'

     #get website url and provides response
     #if error - exits with exception
     try:
         response = requests.get(url)
         response.raise_for_status()

     except HTTPError as httperr:
         print(f"Http error: {httperr}")
         sys.exit(1)
     except Exception as err:
         print(f"Someting went really wrong!: {err}")
         sys.exit(1)

         #change encoding (when open the page with beatiful soup parser it an find information)
         #response.encoding = 'utf-8'
         #soup = bs4(response.text, 'html.parser')

     soup = BeautifulSoup(response.text, 'html.parser')
     #print(f"Worked! \n\n{soup.prettify()}")
     for link in soup.findAll("h3"):
         print(link.div.string)


