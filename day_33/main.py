import requests
import datetime as dt
import smtplib
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = float(data["iss_position"]["longitude"])
# latitude = float(data["iss_position"]["latitude"])
#
# iss_position = (latitude, longitude)
# print(iss_position)

MY_LAT = 37.977978
MY_LON = -122.031075
params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise_hour = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset_hour = data['results']['sunset'].split("T")[1].split(":")[0]

print("sunrise hour", sunrise_hour)
print("sunset hour", sunset_hour)

time_now = dt.datetime.now()

print("time now hour", time_now.hour)