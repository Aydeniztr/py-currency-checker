import os
import sys
from bs4 import Beautifulsoup
import requests

coin = argv[1] 

print(dataparse.prettify())

def get_price(coin):
  
  url = str('https://www.google.com.tr/search?q=%s+price' % coin)

  data = requests.get(url)

  dataparse = Beautifulsoup(HTML.text,'html.parser')
	
	text = dataparse.find(div,attr={'class':''}
