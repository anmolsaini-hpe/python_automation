import json
import requests

people_with_craft_ISS=[]

people_with_craft_Tiangong=[]

def space_data(url):
    request=requests.get(url)
    dump=request.json()
    # print(dump['people'])
    
    for i in dump['people']:
        if (i['craft']) == 'ISS':
            people_with_craft_ISS.append(i['name'])
        elif (i['craft']) == 'Tiangong':
            people_with_craft_Tiangong.append(i['name'])

    print("Total number of persons in ISS " + str(len(people_with_craft_ISS)))
    print("Total number of persons in Tiangong " + str(len(people_with_craft_Tiangong)))






space_data("http://api.open-notify.org/astros.json")