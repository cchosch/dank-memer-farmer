import requests
import json
import time
import random

API_ENDPOINT = "https://discord.com/api/v9"

def read_config():
    try:
        theconfigfile = open("config.json")
        theconfig = json.load(theconfigfile)
        theconfigfile.close()
    except FileNotFoundError:
        print("FATAL ERROR: NO FILE NAMED \"config.json\"")
        quit()
    try:
        theconfig["token"]
    except KeyError:
        print("FATAL ERROR: KEY \"token\" NOT FOUND")
        quit()
    try:
        theconfig["channel-id"]
    except KeyError:
        print("FATAL ERROR: KEY \"channel-id\" NOT FOUND")
        quit()
    try:
      theconfig["pause_timer"]
    except:
      print("FATAL ERROR: KEY \"pause_timer\" NOT FOUND")
      quit()
    return theconfig["token"], theconfig["channel-id"]

TOKEN, CHANNEL_ID = read_config()

def update_glob_vars():
    TOKEN, CHANNEL_ID = read_config()

def main():
    auth_header = {"authorization": TOKEN}
    fishing = {"content":"pls fish"}
    hunting = {"content":"pls hunt"}
    last_fish = time.time()-40
    last_hunt = time.time()-34
    channel_url = API_ENDPOINT+f"/channels/{CHANNEL_ID}/messages"
    res = 0
    while True:
        if time.time()-last_fish > 40:
            res = requests.post(channel_url,headers=auth_header,data=fishing)
            if res.status_code != 201:
              print(res.json())
            last_fish = time.time()-random.uniform(0.1,0.3)
        if time.time()-last_hunt > 40:
            res = requests.post(channel_url,headers=auth_header,data=hunting)
            if res.status_code != 201:
              print(res.json())
            last_hunt = time.time()-random.uniform(0.1,0.3)
            
    
if __name__ == "__main__":
    main()
