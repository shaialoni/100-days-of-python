import os
from dotenv import load_dotenv
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Amazon"

load_dotenv()
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_URL = "https://www.alphavantage.co/query?"
NEWS_URL = "https://newsapi.org/v2/everything?"

today_date = dt.datetime.now().date()
yesterday_date = today_date - dt.timedelta(days=1)
day_before_yesterday = today_date - dt.timedelta(days=2)

yesterday_date = yesterday_date.strftime('%Y-%m-%d')
day_before_yesterday = day_before_yesterday.strftime('%Y-%m-%d')

alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME

}

response = requests.get(ALPHA_URL, params=alpha_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# print(data_list)

# print(data[yesterday_date]['4. close'], data[day_before_yesterday]['4. close'])
yesterday_close = float(data[yesterday_date]['4. close']) #data_list[0]['4. close']
day_before_yesterday_close = float(data[day_before_yesterday]['4. close']) #data_list[1]['4. close']
difference = abs(yesterday_close - day_before_yesterday_close)
percentage_difference = difference / day_before_yesterday_close
print(yesterday_close, day_before_yesterday_close, percentage_difference)

if percentage_difference > 0.03:
    print("yesterday", yesterday_close, "day before", day_before_yesterday_close)
    response = requests.get(NEWS_URL, params=news_params)
    response.raise_for_status()
    news = response.json()['articles'][:3]
    print("Big difference, let's get some news")
    # print(news)
else:
    print("Nothing to see here, move along")

formatted_article_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news]

print(formatted_article_list)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

