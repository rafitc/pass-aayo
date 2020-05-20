import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'http://results.cusat.ac.in/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all('ul')
li = tables[0].find_all('Date of publication')
print(li)
