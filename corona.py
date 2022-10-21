import requests
import datetime
import json

date_now = datetime.datetime.today().strftime('%Y-%m-%dT')
date_week_ago = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime("%Y-%m-%dT")
url = f"https://api.covid19api.com/country/germany?from={date_week_ago}00:00:00Z&to={date_now}00:00:00Z"
# print(date_now)
# print(date_week_ago)

def get_data():
    response = requests.get(url)
    return response.json()

data_last_week = get_data()
data_week_ago = data_last_week[0]
data_today = data_last_week[-1]

if data_today["Active"] > data_week_ago["Active"]:
    trend = "UP"
elif data_today["Active"] > data_week_ago["Active"]:
    trend = "DOWN"
else:
    trend = "PLATEAU"


for day_data in data_last_week:
    if day_data["Active"] > 10000:
        lockdown = True
    elif day_data["Active"] < 10000:
        lockdown = False


data_final = {
    "cases": data_today["Confirmed"],
    "active": data_today["Active"],
    "trend": trend,
    "lockdown": lockdown
}
data_final_json = json.dumps(data_final)

print(data_final_json)
print(data_final)