import requests
import smtplib
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

url = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY_NEW = "c581e79ab49b7f09d8a803bfaf8d5909"
API_KEY = "fcacd7488c5d8bb24fdc556ef3eb2d7f"

#proxy_client = TwilioHttpClient()
#proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['AC84a2db3e64a0cf1b38831d95c38934da']
#auth_token = os.environ.get("2645992786e45a663268a7540e73a40b")
# client = Client(account_sid, auth_token, http_client=proxy_client)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )
#
# print(message.status)
# ----------------------------------------------------------

googleSMTP = "smtp.google.com"
my_gmail = "shai.aloni.dev@gmail.com"
google_password = "wlmdfmttiboouvnd"



lon = -122.0311
lat = 37.978
weather_params = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutley,daily",
    "appid": API_KEY
}
response = requests.get(url, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]
print(hourly_data)

weather_id_list = [item["weather"][0]["id"] for item in hourly_data if item["weather"][0]["id"] < 900]
if len(weather_id_list) > 0:
    print(weather_id_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=google_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="4159800114@vtext.com",
            msg=f"It's working better today!"
        )
    print("Better take an umbrella")




