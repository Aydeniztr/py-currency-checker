#Description: This program gets the price of crypto currencies in real time

#Import the libraries 
from bs4 import BeautifulSoup 
import requests 
import time

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
#Get the URL
    url = "https://www.google.com/search?q="+coin+"+price"
    
    #Make a request to the website
    HTML = requests.get(url) 
  
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser') 
  
    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
#Return the text 
    return text

#Create a main function to consistently show the price of the cryptocurrency
def main():
  #Set the last price to negative one
  last_price = -1
  #Create an infinite loop to continuously show the price
  while True:
    #Choose the cryptocurrency that you want to get the price of (e.g. bitcoin, litecoin)
    crypto = 'bitcoin' 
    #Get the price of the crypto currency
    price = get_crypto_price(crypto)
    #Check if the price changed
    if price != last_price:
      print(crypto+' price: ',price) #Print the price
      last_price = price #Update the last price
    time.sleep(3) #Suspend execution for 3 seconds.
