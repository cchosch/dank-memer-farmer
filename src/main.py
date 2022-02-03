import requests
import json

def read_config():
    theconfigfile = open("config.json")
    theconfig = json.load(theocnfigfile)
    theconfigfile.close()
    return theconfig["token"], theconfig["channelid"]

TOKEN, CHANNEL_ID = read_config()

def update_glob_vars():
    TOKEN, CHANNEL_ID = read_config()

def main():
    auth_header = {"Authorization":f"{TOKEN}"}
    while True:
        pass
    
if __name__ == "__main__":
    main()