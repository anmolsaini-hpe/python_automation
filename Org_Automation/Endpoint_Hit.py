import json
import requests
from socket import timeout
import logging

def hit_endpoint(url):
    list=[]
    if(url!="null"):
        data = requests.get(url)
        #print(data.json())
        # print(data)
        dump = data.json()
        # print(dump)
        for type in dump["people"]:
            print(type['craft'])
            try:
                data2 = requests.get(type['craft'],timeout=10)
                if (data2.status_code==200):
                    list.append(type['craft'])
                    print(list)
                else:
                    print("Status Code is not 200")
            except requests.exceptions.Timeout:
                logging.error("timeout")

    else:
        print("Error loading the url")

hit_endpoint("http://api.open-notify.org/astros.json")
# hit_endpoint("https://www.google.com")
