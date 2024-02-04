import yagmail
import pandas
from news import NewsFeed, content
import datetime
import time
import logging


logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# set the username and password using the content of the apigmailpass.txt file imported from news.py
username = content[1]
password = content[2]


email_content_template = """
Hello {name},

Here's your personalized news about {interest} for today:

{news_content}

Best,
Your News Bot
"""


def send_email():
    try:
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        news_feed = NewsFeed(interest=row['interest'],
                             from_date=yesterday,
                             to_date=today)
        email = yagmail.SMTP(user=username, password=password)
        # format the template with the user's name and their news content
        formatted_email_content = email_content_template.format(name=row['name'],
                                                                interest=row['interest'],
                                                                news_content=news_feed.get())
        email.send(to=row['email'],
                   subject=f"Your {row['interest']} news for today.",
                   contents=formatted_email_content)
        logging.info(f'Email sent successfully to {row["email"]} for {row["interest"]}')
    except Exception as e:
        logging.error(f'Email failed to send to {row["email"]}: {e}')


while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 10:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
