import configme as con
import requests
from cryptography.fernet import Fernet

my_name = con.my_name
key = con.key
url = con.url
fernet = Fernet(key)

print("type '.exit' (without '') to exit.")
if my_name.__len__() != 0:
	requests.post(url, json = { "name": "<<<>>>", "msg": my_name + " has joined the room." } )

while True:
    if my_name.__len__() == 0:
        print("Please edit configme.py and fillup the 'my_name' variable.")
        break

    else:
        msg = input("Enter your Messege: ")
        if msg == ".exit":
            requests.post(url, json = { "name": "<<<>>>", "msg": my_name + " has left the room." } )
            break
        else:
            encMsg = fernet.encrypt(msg.encode()).decode("utf-8")
            response = requests.post(url, json={"name": my_name, "msg": encMsg})
            
            if response.text != "ok":
                print(">>> Message Cannot Send.Try again.")