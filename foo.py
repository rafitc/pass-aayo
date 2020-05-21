import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

URL = 'http://results.cusat.ac.in/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all('ul')
li = tables[1].get_text() #date string start from 131:145
stringStart = li.find(':')
dateOfPub = str(li[(stringStart+1):(stringStart+15)])
pubDate = str(dateOfPub[0:2])
splitDate = dateOfPub.split()
pubMonth = str(splitDate[1])
pubYear = str(splitDate[2])
#print(pubDate)
#print(pubMonth)
#print(pubYear)
s = pubYear,pubMonth,pubDate
st = ' '.join(s)
#print(st)
d = datetime.strptime(st, '%Y %B %d')
da = d.strftime('%Y-%m-%d')

print(da)
#nowDate = datetime.now()

#print("now = ",nowDate,"last pubDate = ",lastPubDate)
#covert into std format

#dateOfPub = dateOfPub.split()
