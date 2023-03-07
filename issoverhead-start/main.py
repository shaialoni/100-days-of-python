import requests
import datetime as dt
import smtplib
import time

googleSMTP = "smtp.google.com"
my_gmail = "shai.aloni.dev@gmail.com"
google_password = "wlmdfmttiboouvnd"
MY_LAT = 37.977978
MY_LON = -122.031075
iss_latitude = 0
iss_longitude = 0


def is_the_iss_near():
    """Return True if ISS is within 5 degrees from my position, False if it's not"""
    global iss_longitude, iss_latitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if 5 >= MY_LAT - iss_latitude >= -5 and 5 >= MY_LON - iss_longitude >= -5:
        print("lon/lat true")
        return True
    else:
        print("lon/lat false")
        return False


def is_it_night():
    """Returns True if current time is past sunset, False if it is not"""
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
    time_now = dt.datetime.now()
    if time_now.hour > sunset_hour:
        return True
    else:
        return False


def send_email():
    print("Sending email")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=google_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="alonishai@gmail.com",
            msg=f"Subject:LOOK UP! ISS is near!!!\n\nCheck this out, ISS is currently at lat: {iss_latitude} lon: {iss_longitude}"
        )


# Your position is within +5 or -5 degrees of the ISS position.

# If the ISS is close to my current position
# and it is currently dark
loop_counter = 1
while True:
    time.now = dt.datetime.now()
    print(f"I ran {loop_counter} times")
    print(f"It is {time.now}")
    time.sleep(60)
    if is_the_iss_near() and is_it_night():
        print(f"Email sent at {time.now}")
        send_email()

    loop_counter += 1

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



