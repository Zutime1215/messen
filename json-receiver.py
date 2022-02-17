import configme as con
import requests
import json
from cryptography.fernet import Fernet
from time import sleep
from datetime import datetime
from pytz import timezone
import pytz

cookies_dict = con.cookie
ozone = con.my_timezone
key = con.crypto_key
time_format = con.date_time_format
url = con.base_url + '/log.json'
t = con.receive_time

# message for valid cookie 
if cookies_dict['__test'].__len__() == 0:
	print("Go To Bakery and make some Cookies and set the cookie in configme.py")


# message for timezone
if ozone.__len__() == 0:
	print("Find out your timezone in timezones.txt file and set it in configme.py")	


# encription staff
fernet = Fernet(key)


timezone = timezone(ozone)

def setTime(t):
	stamptime = int(float(t))
	GMT0 = pytz.utc.localize(datetime.utcfromtimestamp(stamptime))
	return GMT0.astimezone(timezone).strftime(time_format)


j = 0
while True:
	r = requests.get(url, cookies=cookies_dict).text
	message = json.loads(r)
	message_sz = len(message)

	if message_sz == 0:
		print("Looks like there are no message left for Hack!")
		break

	for msg in message[j:]:
		local_time = setTime(msg['id'])

		if msg['nam'] == '<<<>>>':
			print(f"{local_time} :: {msg['nam']} :: {msg['msg']}")
		else:	
			decMessage = fernet.decrypt(bytes(msg['msg'], "utf-8")).decode()
			print(f"{local_time} :: {msg['nam']} :: {decMessage}")	
	
	j = message_sz
	sleep(t)
