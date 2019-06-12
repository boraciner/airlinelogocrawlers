import requests
import urllib.request
from bs4 import BeautifulSoup

baseUrl = 'https://www.seatguru.com/browseairlines/browseairlines.php'
page = requests.get(baseUrl)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.title)

airlineslinks = soup.find_all('a', href=True)

for link in airlineslinks:
  if "airlines" in link['href']:
    inurl = "https://www.seatguru.com/airlines"+link['href']
    inpage = requests.get(inurl)
    soup2 = BeautifulSoup(inpage.text)
    span = soup2.find('span',{'class':'ai-info'})
    if span is not None:
      print(span.text)	
      urllib.request.urlretrieve("https://cdn.seatguru.com/en_US/img/20190523194706/seatguru/airline_logos/"+span.text+".jpg", span.text+".jpg")
