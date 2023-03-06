##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

googleSMTP = "smtp.google.com"
my_gmail = "shai.aloni.dev@gmail.com"
google_password = "wlmdfmttiboouvnd"


# Check if today matches a birthday in the birthdays.csv
# I decided to use dict comprehension to create a dict with
df = pandas.read_csv("birthdays.csv")
birthdays = df
today = dt.datetime.now()
print(birthdays)
birthdays_today = [(item['name'], item['email']) for i, item in birthdays.iterrows() if item['day'] == today.day and item['month'] == today.month]
print(birthdays_today)

# If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in birthdays_today:
    print(person)
    random_letter_number = random.randint(1, 3)
    with open(f"./letter_templates/letter_{random_letter_number}.txt", "r") as file:
        filedata = file.read()

    filedata = filedata.replace("[NAME]", f"{person[0]}")

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=google_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=f"{person[1]}",
            msg=f"Subject:Happy Birthday!!!\n\n{filedata}"
        )



