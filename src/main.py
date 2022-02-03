import requests
import json
import time
import random

API_ENDPOINT = "https://discord.com/api/v9"

def read_config():
    theconfigfile = open("config.json")
    theconfig = json.load(theconfigfile)
    theconfigfile.close()
    return theconfig["token"], theconfig["channel-id"]

TOKEN, CHANNEL_ID = read_config()

def update_glob_vars():
    TOKEN, CHANNEL_ID = read_config()

def main():
    print(CHANNEL_ID)
    auth_header = {"authorization": TOKEN}
    fishing = {"content":"pls fish"}
    hunting = {"content":"pls hunt"}
    last_fish = time.time()-40
    last_hunt = time.time()-34
    channel_url = API_ENDPOINT+f"/channels/{CHANNEL_ID}/messages"
    while True:
        if time.time()-last_fish > 40:
            print(requests.post(channel_url,headers=auth_header,data=fishing))
            last_fish = time.time()+random.uniform(0.1,0.3)
        if time.time()-last_hunt > 40:
            print(requests.post(channel_url,headers=auth_header,data=hunting))
            last_hunt = time.time()+random.uniform(0.1,0.3)
            
    
if __name__ == "__main__":
    main()
