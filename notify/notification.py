cookies_dict = {'__test': '299447a688f0c4c833fc1ad410d426ef'}
key = 'vP1nWwtTo6in4-CqvOM_J3l0sXSebiJRk2n_tV1luCk='
my_timezone = 'Asia/Dhaka'

import requests
import json
from cryptography.fernet import Fernet
import os
from time import sleep

url = 'http://willnervegearbeeofficial411333206873787.rf.gd/json-test/log.json'

# encription staff
fernet = Fernet(key)

while True:
	r = requests.get(url, cookies=cookies_dict).text
	messege = json.loads(r)

	with open('last_epoch.txt', 'r') as r:
		epoch = float(r.read())
		
	if float(messege[-1]['id']) > epoch:
		last_messen = messege[-1]['nam']
		if last_messen == '<<<>>>':
			last_msg = "Somebody Joined The Room"
		else:
			last_msg = fernet.decrypt(bytes(messege[-1]['msg'], "utf-8")).decode()

		os.system(f'/home/zahid/Public/messen-v1.2/notify/notification.sh "{last_messen}: {last_msg}"')
	epoch = messege[-1]['id']	
	with open('last_epoch.txt', 'w') as w:
		w.write(epoch)
	sleep(30)
