import requests
from bs4 import BeautifulSoup
import time

smsURL = "https://www.fast2sms.com/dev/bulk"    #FAST2SMS for sms notification
API_KEY = "YourApiKey"
sendNump = "SendNumber"	#To Number


def initalSendReq():
	URL = 'http://results.cusat.ac.in/'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	tables = soup.find_all('ul')
	initialCount = len(tables)
	return initialCount


def updateResult():
	URL = 'http://results.cusat.ac.in/'
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

