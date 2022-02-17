import configme as con
import requests
import datetime
from cryptography.fernet import Fernet

nam = con.my_name
cookies_dict = con.cookie
key = con.crypto_key
url = con.base_url + '/config.php'

# message for valid cookie 
if cookies_dict['__test'].__len__() == 0:
	print("Go To Bakery and make some Cookies and set the cookie in configme.py")
	


def makeID():
	return datetime.datetime.now().timestamp()

print("type '.exit' (without '') to exit.")

# encription staff
fernet = Fernet(key)


# member joining message
if nam.__len__() != 0:
	requests.get(url+f"?iD={makeID()}&name=<<<>>>&msg={nam} join the room.", cookies=cookies_dict)


with requests.Session() as r:

	while True:
		if nam.__len__() == 0:
			print("Please edit configme.py and fillup the 'my_name' variable.")
			break
		else:	
			msg = input("Enter your Messege: ")

			if msg == ".exit":
				# r.get(url+f"?iD={makeID()}&name=<<<>>>&msg={nam} has left the room.", cookies=cookies_dict)
				break
			else:
				encMessage = fernet.encrypt(msg.encode())	
				messenger = {'iD': makeID() ,'name': nam , 'msg': encMessage}
				if msg != "":
					r.get(url, params=messenger, cookies=cookies_dict)