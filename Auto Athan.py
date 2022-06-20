import requests
import json

params = {"longitude": -79.556109, "latitude": 43.826185, "date_or_timestamp": "17-06-2022", "annual": False, "method": 2, "school": 0}
# response = requests.get("http://api.aladhan.com/v1/calendar", params=params)

response = requests.get("http://api.aladhan.com/v1/timings/:date_or_timestamp", params=params)

athan = response.json()

print(type(athan))

thetime = athan['data']['timings']['Fajr']
print(thetime)
# new_string = json.dumps(athan, indent=2)
# print(type(new_string))
#
# print("klfdjglfjlg")
#
# print(new_string)


