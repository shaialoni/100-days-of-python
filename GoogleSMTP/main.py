import smtplib

googleSMTP = "smtp.google.com"
yahooSMTP = "smtp.mail.yahoo.com"
my_gmail = "shai.aloni.dev@gmail.com"
my_yahoo = "shaialoni.dev@yahoo.com"
google_password = "wlmdfmttiboouvnd"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_gmail, password=google_password)
#     connection.sendmail(
#         from_addr=my_gmail,
#         to_addrs=my_yahoo,
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1980, month=10, day=16, hour=10)
# print(date_of_birth)

import datetime as dt
import random

if dt.datetime.now().weekday() == 2:
    print("sending")
    with open("quotes.txt") as file:
        quotes = file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=google_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="4159800114@vtext.com",
            msg=f"Subject:Today's Motivational Quote\n\n{random.choice(quotes)}"
        )
