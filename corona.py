import requests
import datetime
import json

def corona_data_last_week():

    date_now = datetime.datetime.today().strftime('%Y-%m-%dT')
    date_week_ago = (datetime.datetime.today() - datetime.timedelta(days=21)).strftime("%Y-%m-%dT")
    url = f"https://api.covid19api.com/country/germany?from={date_week_ago}00:00:00Z&to={date_now}00:00:00Z"

    def get_data():
        response = requests.get(url)
        return response.json()

    data_last_3_weeks = get_data()
    data_3_weeks_ago = data_last_3_weeks[0]
    data_2_weeks_ago = data_last_3_weeks[-15]
    data_week_ago = data_last_3_weeks[-8]
    data_today = data_last_3_weeks[-1]
    active_today = data_today["Active"] - data_2_weeks_ago["Active"]
    active_week_ago = data_week_ago["Active"] - data_3_weeks_ago["Active"]

    if active_today > active_week_ago:
        trend = "UP"
    elif active_today < active_week_ago:
        trend = "DOWN"
    else:
        trend = "PLATEAU"


    last_week_confirmed = []
    first_week_confirmed = []
    last_week_active = []

    for index, day_data in enumerate(data_last_3_weeks):
        if index > 13:
            last_week_confirmed.append(day_data["Active"])
        if index < 7:
            first_week_confirmed.append(day_data["Active"])

    for item in range(len(last_week_confirmed)):
        last_week_active.append(last_week_confirmed[item] - first_week_confirmed[item])

    for active in last_week_active:
        if active > 10000:
            lockdown = True
            break
        else:
            lockdown = False 

    data_final = {
        "cases": data_today["Confirmed"],
        "active": active_today,
        "trend": trend,
        "lockdown": lockdown
    }

    data_final_json = json.dumps(data_final)

    return data_final_json
