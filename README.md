# airlinelogocrawlers
Python script for crawing www.seatguru.com to download airline company logos





import requests
import urllib.request
import string
from bs4 import BeautifulSoup
import time
import sys

letter = str(sys.argv[1])
print("LETTER "+letter)
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
baseUrl = 'https://www.wego.com.tr/en/airlines/'+letter
page = requests.get(baseUrl, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')


images = soup.findAll('img')
finalImageLinks = []
for image in images:
  if "airlines_square" in image['src']:
    finalImageLinks.append(str(image['src'].replace("w_30,h_27,f_auto,fl_lossy,q_80","f_auto,fl_lossy,h_90,w_90,q_600")))
  
myAirlineTag = soup.find_all('ul', 'airlines-in-location')

finalAircraftCompanies = []
for searchInTag in myAirlineTag:
  airlineslinks = searchInTag.find_all('a', href=True)
  for airlineslink in airlineslinks: 
    finalAircraftCompanies.append(str(airlineslink.contents[0]))


index=0
for finalImageLink in finalImageLinks:
  print(finalImageLink)
  urllib.request.urlretrieve(finalImageLink, finalAircraftCompanies[index]+".png")
  index+=1
