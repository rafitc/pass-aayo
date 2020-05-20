import requests
from bs4 import BeautifulSoup
import re
#from datetime import datetime

URL = 'http://results.cusat.ac.in/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all('ul')
li = tables[0].get_text() #date string start from 131:145
stringStart = li.find(':')
dateOfPub = str(li[(stringStart):(stringStart+15)])

print(dateOfPub)
#dateOfPub = dateOfPub.split()
