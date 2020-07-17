#url https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid={YOUR API KEY}

import json
import requests
import numpy as np


BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"
CITY = "Ottawa"
API_KEY = "68614c20e4464baf63a8e463581321bd"
LONGITUDE = "-75.85"
LATITUDE = "45.28"

# upadting the URL
url = BASE_URL + "lat=" + LATITUDE + "&lon=" + LONGITUDE + "&exclude=minutely" + "&appid=" + API_KEY


#url = "https://api.openweathermap.org/data/2.5/forecast?lat=45.28&lon=-75.85&exclude=current,minutely,&appid=68614c20e4464baf63a8e463581321bd"

print(url)

response = requests.get(url)

info = response.json()

info_str = json.dumps(info, indent=2)

rain_array = empty((0,24))
sum_rain = 0
rainData = 0
n = 0      
print("Expected Rain (mm)\n")

for item in info.items():
    for x in info["hourly"]:
        try:
            rainData = info["hourly"][n]["rain"]["1h"]     #pull information about how much rain is expected
            print("in {0} hours, {1}mm is expected".format(n+1,rainData))   #print information about how much rain is expected and when
        except:
            pass                                   #have the code continue when rain data is not available for that timestamp
         
        n = n+1

rain_array.append(rainData)
sum_rain = sum_rain + rainData
print(sum_rain)
print(rain_array)


#print(n,info["list"].index(100),info["list"][n]["clouds"])
#print(info_str)