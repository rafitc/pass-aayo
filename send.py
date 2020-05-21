import requests

url = "https://www.fast2sms.com/dev/bulk"
YOUR_API_KEY = "3Qgitp2fNMEyqr4APUjlR1Twzn5eBuv97LXsVkDJxIG8bdKOaS2wRAOZGYitmao49xN7UTEW6czJIDSB"


querystring = {"authorization":YOUR_API_KEY,"sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":"7907348448"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)