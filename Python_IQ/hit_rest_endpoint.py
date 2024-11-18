import json 
import requests
from socket import timeout

url_list=[]
def hit_endpoint(url):
    data=requests.get(url)
    dump=data.json()

    for list in dump:
        placeholders_url=list['url']
        data2=requests.get(placeholders_url,timeout=10)

        try:
            if data2.status_code==200:
                url_list.append(placeholders_url)
            else:
                print("Status code is not 200")
        except TimeoutError as error:
            print(error)








if __name__=="__main__":
    hit_endpoint("https://jsonplaceholder.typicode.com/photos")
