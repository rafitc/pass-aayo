import requests
from bs4 import BeautifulSoup
import time
import os

from dotenv import load_dotenv
load_dotenv()

smsURL = os.getenv('SMS_PROVIDER_URL')
API_KEY = os.getenv('API_KEY')
sendNump = os.getenv('TO_NUMBER')	#To Number


def initalSendReq():
	URL = 'https://results.cusat.ac.in'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	print(soup)
	tables = soup.find_all('ul')
	initialCount = len(tables)
	return initialCount


def updateResult():
	URL = 'https://results.cusat.ac.in/'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	tables = soup.find_all('ul')
	message = tables[0].get_text()
	print(tables[0].get_text())
	return message


def compare(currentCount, oldCount):
	if(currentCount>oldCount):
		print("Result Updated !")
		update = True
	else:
		update = False
		print("No updates !")
	return update


def sendSms():
	querystring = {
		"authorization": API_KEY,
		"sender_id": "FSTSMS",
		"message": message,
		"language": "english",
		"route": "p",
		"numbers": sendNump
	}
	headers = {
		'cache-control': "no-cache"
	}
	response = requests.request("GET",smsURL, headers=headers, params=querystring)
	print(response)


print("CUSAT exam result notification :")
old = initalSendReq()

while True:
	time.sleep(3)
	now = initalSendReq()
	update = compare(now, old)
	if update:
		message = updateResult()
		sendSms()
		old = now

