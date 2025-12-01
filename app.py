import tweepy
import os
import feedparser
from datetime import datetime

client = tweepy.Client(
    consumer_key=os.getenv("TW_API_KEY"),
    consumer_secret=os.getenv("TW_API_SECRET"),
    access_token=os.getenv("TW_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TW_ACCESS_TOKEN_SECRET")
)

def post_test():
    try:
        client.create_tweet(text=f"Test from Railway! {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("Posted successfully!")
    except Exception as e:
        print("Error:", e)

post_test()
