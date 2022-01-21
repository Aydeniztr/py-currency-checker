#Description: This program gets the price of crypto currencies in real time
#Import the libraries
from bs4 import BeautifulSoup
import requests
import time
#Create a function to get the price of a cryptocurrency
coin = input('give the name of the cryptocurrency you want to check\n>>')
#Get the URL
url = "https://www.google.com/search?q="+coin+"+price"
#Make a request to the website
HTML = requests.get(url)
#Parse the HTML
soup = BeautifulSoup (HTML. text, 'html.parser')
#Find the current price
#text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
#Return the text
print(coin + [price] -> '+ text)

