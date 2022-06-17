import requests

params = {"longitude": -79.556109, "latitude": 43.826185, "date_or_timestamp": "17-06-2022", "annual": False, "method": 2, "school": 0}
# response = requests.get("http://api.aladhan.com/v1/calendar", params=params)

response = requests.get("http://api.aladhan.com/v1/timings/:date_or_timestamp", params=params)

print(response.json())
