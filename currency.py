
from colorama import Fore,Back,Style,init,deinit
from bs4 import BeautifulSoup
import requests
import time
import sys

init()

banner = '''
 __        __   __   ___       __          __        ___  __        ___  __  
/  ` |  | |__) |__) |__  |\ | /  ` \ / __ /  ` |__| |__  /  ` |__/ |__  |__) 
\__, \__/ |  \ |  \ |___ | \| \__,  |     \__, |  | |___ \__, |  \ |___ |  \ 
                                                                             

author : Ahmet Yigit AYDENIZ
'''
if len(sys.argv) <= 1:
	
	print(banner)
	exit()

else:

	print('\n'+ banner +'\n')
	
	if sys.argv[1] == 'list':
		
		while True:
		
			with open ("stocks.txt", "r") as myfile:
				data = myfile.read().splitlines()

			for i in data:
    	
				url = "https://www.google.com/search?q="+i+"+price"

				HTML = requests.get(url)
	
				named_tuple = time.localtime()
	
				time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

				soup = BeautifulSoup (HTML. text, 'html.parser')
				
				text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
				
				if '+' in text:
					print(i + Fore.GREEN +' '+text+Fore.RESET+' '+time_string)
				elif '-' in text:
					print(i + Fore.RED +' '+ text +Fore.RESET+' '+time_string)
				else:
					print(i + Fore.YELLOW +' [price] -> '+ text +Fore.RESET+' '+time_string)
			else:
				print("")

		time.sleep(3)

	else:
		stock = sys.argv[1]

		url = "https://www.google.com/search?q="+stock+"+price"

		while True:

			HTML = requests.get(url)
	
			named_tuple = time.localtime()
	
			time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

			soup = BeautifulSoup (HTML. text, 'html.parser')

			text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

			if '+' in text:
				print(stock + Fore.GREEN +' '+text+Fore.RESET+' '+time_string)
			elif '-' in text:
				print(stock + Fore.RED +' '+ text +Fore.RESET+' '+time_string)
			else:
				print(stock + Fore.YELLOW +' [price] -> '+ text +Fore.RESET+' '+time_string)
	
			time.sleep(3)

deinit()
