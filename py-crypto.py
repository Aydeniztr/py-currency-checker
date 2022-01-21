import os
import sys
from bs4 import Beautifulsoup
import requests

coin = argv[1] 

def get_price(coin):
  
  url = str('https://www.google.com.tr/search?q='+ coin +'+price')

  data = requests.get(url)

  dataparse = Beautifulsoup(HTML.text,'html.parser')
	
  # <div class="H0PQec">
  # <div class="sbc esbc">
	
  text = dataparse.find(div,attr={'class':'H0PQec'}.find(div,attr={'class':'sbc esbc'}.text
							 
  return text
							   
