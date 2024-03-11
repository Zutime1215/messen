import pytz
import json
import requests
import configme as con
from time import sleep
from pytz import timezone
from datetime import datetime
from cryptography.fernet import Fernet

my_timezone = con.my_timezone
date_time_format = con.date_time_format
key = con.key
url = con.url
my_name = con.my_name
receive_time = con.receive_time

fernet = Fernet(key)
timezone = timezone(my_timezone)

def setTime(t):
	stamptime = int(float(t))
	GMT0 = pytz.utc.localize(datetime.utcfromtimestamp(stamptime))
	return GMT0.astimezone(timezone).strftime(date_time_format)

# if my_name.__len__() != 0:
# 	requests.post(url, json = { "name": "<<<>>>", "msg": my_name + " has joined the room." } )

j = 0
while True:
    r = requests.get(url).text
    message = json.loads(r)
    message_sz = len(message)

    if message_sz == 0:
        print("Looks like there are no message left for Hack!")
        break

    for msg in message[j:]:
        local_time = setTime(msg['id'])

        if msg['name'] == '<<<>>>':
            print(f"{local_time} :: {msg['name']} :: {msg['msg']}")
        else:
            decMessage = fernet.decrypt(bytes(msg['msg'], "utf-8")).decode()
            print(f"{local_time} :: {msg['name']} :: {decMessage}")
    
    j = message_sz
    sleep(receive_time)