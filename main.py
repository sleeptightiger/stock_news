import requests
from datetime import date, timedelta
from twilio.rest import Client


STOCK_NAME = "IBM"
COMPANY_NAME = "IBM"




NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API = "H95KVEHLKT48JEGA"
NEWS_API = "25dc005829994685b707af6831bf98cc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"

NEWS_PARAMETERS = {
    'qInTitle': COMPANY_NAME,
    'from': date.today(),
    'sortBy': 'popularity',
    'apiKey': NEWS_API
 }

ALPHA_VANTAGE_PARAMETERS = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'outputsize': 'compact',
    'apikey': ALPHA_VANTAGE_API
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def get_news(percentage_diff, stock_diff, STOCK_NAME, COMPANY_NAME):
    account_sid = 'ACf22f4ffa32d290a001af369f6455cb71'
    auth_token = '775bf42dd1c9bf8bdb33027c906d6df4'
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    response.raise_for_status()
    data = response.json()
    three_articles = data['articles'][:3]
    formatted_articles = [f"\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    icon = ''
    if stock_increase:
        icon = '🔺'
    else:
        icon = '🔻'
    text = f"{COMPANY_NAME}: {icon}{int(percentage_diff)}%'\n'"
    for article in formatted_articles:
        text += article
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=text,
        from_='+15102408628',
        to='+19563265811'
    )





response = requests.get(STOCK_ENDPOINT, params=ALPHA_VANTAGE_PARAMETERS)
response.raise_for_status()
data = response.json()
yesterday = str(date.today() - timedelta(days=1))

days = list({key:value for (key, value) in data['Time Series (Daily)'].items()})

yesterday_closing = float(data['Time Series (Daily)'][days[0]]['4. close'])
day_before_yesterday_closing = float(data['Time Series (Daily)'][days[1]]['4. close'])

stock_diff = day_before_yesterday_closing - yesterday_closing
max = max(day_before_yesterday_closing, yesterday_closing)
min = min(day_before_yesterday_closing, yesterday_closing)
percentage_diff = 100 - (min / (max/100))
stock_increase = False
if stock_diff < 0:
    stock_increase = True

if percentage_diff >= 5:
    get_news(percentage_diff, stock_diff, STOCK_NAME, COMPANY_NAME)