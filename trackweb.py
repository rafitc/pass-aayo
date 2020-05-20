import requests
from bs4 import BeautifulSoup
from datetime import datetime
URL = 'http://results.cusat.ac.in/'
page = requests.get(URL)
"""
soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all('ul')
latest = 0
last = (len(tables) - 1)
count = 0
"""

#link = tables[latest].find('a')
#print(link.get_text())

def checkUpdate(): #function to check is there any 
	print("checking ")
	now = datetime.now() 
	print("today is ",now)

checkUpdate()

"""
t = soup.find('ul')
print(t.get_text())
"""